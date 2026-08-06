import hapy.models as models
import hapy.helpers as helpers
from hapy.config import settings


logger = helpers.get_logger('status')


def report(state, **attributes):
    """Push an app status entity to Home Assistant so failures are visible on a dashboard."""
    if not settings.status_entity_id:
        return
    attributes['reported_at'] = helpers.get_now().isoformat()
    try:
        models.EntityHandler.homeassistant.set_state(
            entity_id=settings.status_entity_id,
            data={'state': state, 'attributes': attributes}
        )
    except Exception as e:
        logger.error(f'[STATUS] - failed to report status to HA: {e}')
