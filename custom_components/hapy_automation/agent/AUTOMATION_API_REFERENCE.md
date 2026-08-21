# Guía de referencia: escribir automatizaciones con hapy_automation

Referencia para el agente (y cualquier humano) antes de escribir o modificar
código en el repo de automatizaciones. No es documentación de usuario del
paso a paso de instalación — eso está en el README de `hapy-automation`.

## Antes que nada: no es un framework genérico

`hapy.Automation` **no** es algo que se instancie directamente ni que
exponga métodos sueltos tipo `get_state()`/`call_service()`/`trigger()`. Si
lo que estás a punto de escribir se parece a esto, está mal — es una API
inventada, no la real:

```python
# ❌ MAL — esto no es hapy.Automation, no hace absolutamente nada
from hapy import Automation

automation = Automation()

def set_water_heater_state(new_state):
    economizer_state = automation.get_state('input_boolean.water_heater_energy_saving')
    ...

automation.trigger(input_boolean_entity_id='input_boolean.guest_mode', event='state_changed', callback=set_water_heater_state)
```

Esto falla en silencio de dos formas a la vez: `Automation` no tiene esos
métodos (ni falta que hacen), y aunque los tuviera, un fichero así **nunca
se ejecuta** porque no define ninguna subclase — no hay nada que el
mecanismo de binding pueda descubrir. La forma correcta es una **subclase**
de `hapy.Automation` con `init_condition()`/`action()`, ver la sección
siguiente y el ejemplo completo más abajo.

## Estructura del repo

- Un paquete `automations/` en la raíz, con un `__init__.py` que importa
  todos sus submódulos (`from .kitchen import *`, etc.) — así es como se
  descubren las automatizaciones, no hay registro manual en ningún sitio.
  **Un módulo nuevo que no aparezca en `__init__.py` no se ejecuta nunca,
  aunque su código sea perfecto** — no produce ningún error (el reload da
  "ok" igualmente, porque no hay nada roto que falle: simplemente el
  fichero no se toca), así que este fallo es silencioso y fácil de no
  detectar. `write_automation_file` añade esta línea automáticamente
  cuando el fichero es `automations/<nombre>.py` directo (no anidado) y
  aún no está importado — pero comprueba siempre la nota que devuelve la
  herramienta, y si la estructura no es el caso simple (subpaquetes,
  etc.), añade el `import` tú mismo con `write_automation_file` sobre
  `automations/__init__.py`.
- Cualquier otro paquete auxiliar (`helpers/`, constantes, etc.) es Python
  normal, importable desde los módulos de `automations/`.
- **Nunca** se escriben a mano ni se comitean `entities.py`, `devices.py`,
  `domains.py` — se regeneran en cada recarga a partir del estado real de
  Home Assistant. Si existen en el repo por el sistema antiguo, son ruido.

## La clase `Automation`

```python
import hapy
import entities
import devices


class OnMySwitchOn(hapy.Automation):

    def init_condition(self):
        return devices.MySwitch.remote_button_short_press_turn_on

    def action(self):
        entities.MyLight.services.turn_on()

    def exit_condition(self):          # opcional
        return devices.MySwitch.remote_button_long_release_dim_up
```

- `init_condition()` se reevalúa cada vez que cambia algo a lo que la
  automatización está vinculada. El binding (a qué entidades/dispositivos
  reacciona) se calcula automáticamente, en el momento en que la clase se
  define, ejecutando `init_condition()` una vez en "modo descubrimiento" y
  observando qué `entities.X`/`devices.Y` toca — **no hay que declarar
  explícitamente a qué reacciona una automatización.**
- Si `init_condition()` devuelve `True`, se ejecuta `action()`.
- `exit_condition()` (opcional, por defecto `True`) mantiene `action()`
  corriendo en bucle (cada `step_time` segundos, hasta `timeout` segundos)
  mientras devuelva `False` — útil para "mientras se mantiene pulsado un
  botón".
- El nombre de la clase debe ser único y descriptivo (`OnDiningMainSwitchOn`,
  no `Automation1`).

### Importante: `or`-chains en `init_condition()`

Es idiomático escribir condiciones como:

```python
def init_condition(self):
    return (
        entities.SensorEsiosPvpcHapy.state.changed()
        or entities.InputBooleanWashingPending.state.changed()
        or entities.InputBooleanWashingUrgent.state.changed()
    )
```

Esto es seguro: el binding se calcula en un modo especial donde
`.changed()`/`.updated()` siempre devuelven `False`, así que el `or` nunca
corta antes de tocar todos los operandos — todas las entidades de la cadena
quedan correctamente vinculadas, no solo la primera. No hace falta escribir
esto como sentencias separadas para "forzar" el binding.

## Acceso a entidades — `entities.X`

- `entities.X.state.state_value` — valor actual del estado.
- `entities.X.state.old.state_value` — valor anterior.
- `entities.X.state.<atributo>` — cualquier atributo del estado
  (Pythonizado: `brightness_pct`, no `brightness-pct`).
- `entities.X.state.changed(old_value=None, new_value=None, offset=60)` —
  `True` si cambió al valor esperado (o a cualquier valor nuevo si no se
  especifica) en los últimos `offset` segundos.
- `entities.X.state.updated(attribute, old_value=None, new_value=None, seconds=5)`
  — igual pero sobre un atributo concreto, no el estado principal.
- `entities.X.services.<nombre_servicio>(**kwargs)` — llama al servicio de
  Home Assistant del dominio de esa entidad (p.ej. `light.turn_on` para una
  `light.X`). Los nombres/parámetros exactos disponibles se pueden consultar
  con la herramienta `list_states`/`get_state` para ver el dominio, o
  preguntando directamente por el servicio si hay duda — no inventar
  parámetros de servicio.

## Acceso a dispositivos Zigbee — `devices.X`

- `devices.X.<trigger>` — booleano que se pone a `True` momentáneamente
  cuando salta un trigger de dispositivo ZHA (pulsación corta/larga de un
  mando, etc.), y vuelve a `False` tras el ciclo. El nombre exacto del
  trigger depende del dispositivo — consultarlo listando el fichero
  `devices.py` generado (herramienta `read_automation_file` no aplica
  aquí porque `devices.py` no vive en el repo del usuario; en su lugar,
  preguntar al usuario o usar `list_states`/inspección si hace falta
  confirmar el nombre exacto de un trigger).
- Requiere que el dispositivo esté gestionado por la integración `zha` y
  que su quirk defina `device_automation_triggers`.

## Patrones útiles ya usados en este proyecto

- **Helper compartido con estado** (`helpers/lights.py`, `LightChain`):
  construir un objeto a nivel de módulo que encapsula varias entidades
  relacionadas (p.ej. un grupo de luces) y reutilizarlo desde varias
  automatizaciones.
- **Herencia entre automatizaciones** (`automations/climate.py`,
  `LivingAc(OfficeAc)`): cuando dos automatizaciones comparten toda la
  lógica y solo cambian qué entidades usan, hereda de la base y
  sobreescribe solo los atributos de clase (`ac`, `switch`, `max_temp`,
  etc.), no el método `action()` entero.
- **Estado compartido entre automatizaciones vía atributo de clase**
  (`automations/living.py`, `OnTvTurnedOn`/`OnTvTurnedOff`): una
  automatización puede leer/escribir un atributo de clase de otra para
  coordinarse, cuando tiene sentido que compartan un flag.

## Antes de dar una tarea por terminada

1. Escribe/edita el fichero con `write_automation_file`.
2. Haz `git_commit_and_push` con un mensaje de commit claro.
3. **Comprueba el resultado real que te devuelve** (`reload_ok`/
   `reload_error`) — un push que rompe la sintaxis o referencia una
   entidad que no existe hace que el sistema haga rollback automáticamente
   a la última versión buena; si eso pasa, el error te dice por qué,
   corrígelo y vuelve a intentarlo en la misma conversación antes de
   responder al usuario que ya está hecho.
4. Si la tarea implica acciones sobre climatización, riego, cierres u
   otros sistemas con impacto físico real, confirma con el usuario antes
   de hacer push si la petición era ambigua.
5. `reload_ok` en `True` confirma que el código importa y no rompe nada —
   **no confirma que la automatización nueva esté realmente conectada ni
   que haga lo que se pidió**. Antes de decir que está hecho, verifica
   además con `read_automation_file` que `automations/__init__.py`
   importa el módulo nuevo, y que la clase usa de verdad `init_condition()`/
   `action()` sobre `entities.X`/`devices.X` (no la API inventada de la
   sección "Antes que nada" de arriba) — un fichero bien escrito pero no
   importado, o con una API que no existe, no da ningún error y no hace
   absolutamente nada.
