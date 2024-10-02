#!/bin/sh

EMAIL="$EMAIL_ADDRESS"

sudo apt-get install mailutils
echo "A variável EMAIL_ADDRESS está definida como: " $EMAIL
echo "Atualização Código S107" | mail -s "prezado, boa noite! Apenas passando para lhe informar que existe uma nova versão do código de S107 do Vitor e Gabriel. Att, Chris" $EMAIL