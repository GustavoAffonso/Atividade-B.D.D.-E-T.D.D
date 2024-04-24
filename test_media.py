from Media import Media
def test_media_simples(self):
  result = Media.media(1, 5)
  assert result == 5
  
def test_media_negativa(self):
  result = Media.media(-6, -4)
  assert result == -1

def test_media_mista(self):
  result = Media.media(8, -4)
  assert result == 5

def test_media_decimal(self):
  result = Media.media(0.7, 0.5)
  assert result == 6