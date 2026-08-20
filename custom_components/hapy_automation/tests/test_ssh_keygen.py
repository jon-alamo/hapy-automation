"""Real ssh-keygen invocation (not mocked) — confirms a usable ed25519
keypair actually gets written, and that calling generate_keypair() again
for the same path reuses it instead of silently overwriting it with a
different key (which would orphan whatever the user already added as a
deploy key on GitHub)."""
import os
import tempfile

from custom_components.hapy_automation.ssh_keygen import generate_keypair


def test_generates_a_real_usable_keypair():
    with tempfile.TemporaryDirectory() as tmp:
        key_path = os.path.join(tmp, 'id_ed25519')
        public_key = generate_keypair(key_path, comment='test@hapy')

        assert os.path.isfile(key_path)
        assert os.path.isfile(key_path + '.pub')
        assert public_key.startswith('ssh-ed25519 ')
        assert 'test@hapy' in public_key
        # Private key should not be group/world readable.
        assert oct(os.stat(key_path).st_mode)[-3:] == '600'


def test_calling_again_reuses_the_existing_key_instead_of_regenerating():
    with tempfile.TemporaryDirectory() as tmp:
        key_path = os.path.join(tmp, 'id_ed25519')
        first = generate_keypair(key_path, comment='test@hapy')
        second = generate_keypair(key_path, comment='test@hapy')
        assert first == second
