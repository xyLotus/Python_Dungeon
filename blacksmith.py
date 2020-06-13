import start, clear, player_stats
import os, random, sys

def shop():
    clear.trigger()
    print("""
                      `yNms/`
                    :ydMMMMMm
                    oMMMMMMN-
                   .dMMMMMNNNho:``
                   :ymNMMd-:odNNNho:``
                      -/s.    `:ohmNNho:.`
                                  `:ohmNNho:.`
                                      `:ohmNNho:.`
                                          .:ohmNNy
                                              .:+-


                `::::::::::::::::::::::::::::`
+yysyyyyyyyyyyyddMMMMMMMMMMMMMMMMMMMMMMMMMMMM-      1) Upgrade Sword
`smmhhdmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdh.      2) Upgrade Armor
  ./syyo+++oossmMMMMMMMMMMMMMMMMMMMMNhs/-.``        3) Exit
     `..-:/+++odMMMMMMMMMMMMMMMMMMNo.`
             ``.-+hMMMMMMMMMMMMMMM:
                  `+MMMMMMMMMMMMMN
                    mMMMMMMMMMMMMM.
                   -NMMMMMMMMMMMMMm:
               `:ohNMMMd+-...-:yNMMNdo-
               .NNNNNNh`        /NNNNNd
    """)

    option = int(input("<option> "))
