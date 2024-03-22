DELIMITER | -- Permet l'utilisation du point-virgule dans le code du trigger
CREATE TRIGGER check_valid_email BEFORE UPDATE ON users FOR EACH ROW -- Crée un déclencheur qui se déclenche avant la mise à jour de la table users pour chaque ligne affectée
BEGIN -- Début du bloc d'instructions du déclencheur
  IF NEW.email <> OLD.email THEN -- Vérifie si le nouvel e-mail est différent de l'ancien e-mail
    SET NEW.valid_email = 0; -- Définit la colonne valid_email de la nouvelle ligne comme 0 (faux) si l'e-mail change
  END IF; -- Fin de la condition IF
END; -- Fin du bloc d'instructions du déclencheur
| -- Fin du bloc de code du déclencheur
DELIMITER ; -- Rétablit le délimiteur par défaut
