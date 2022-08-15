from django.forms import ModelForm
from .models import Transacao


class TrasacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = [ "descricao", "valor", "observacoes", "categoria"]