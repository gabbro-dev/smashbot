import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from mainCode import Players, getArgRankProfiles, rows

# Get all profiles
print("Launching bot")
print("=" * 100)
getArgRankProfiles()

# Para que solo funcione en un server (Discord tarda 1 hora aprox para actualizar slash commands si no)
testServerId = 858156171704795136 # <--- Server de Los Panitas
# Smash Bros Roster Stock Icons
ssbuRosterStockImg = {"Mario": "https://braacket.com/assets/images/game/ssbu/characters/mario.png",
                 "Donkey Kong": "https://braacket.com/assets/images/game/ssbu/characters/donkey_kong.png",
                 "Link": "https://braacket.com/assets/images/game/ssbu/characters/link.png",
                 "Samus": "https://braacket.com/assets/images/game/ssbu/characters/samus.png",
                 "Dark Samus": "https://braacket.com/assets/images/game/ssbu/characters/darksamus.png",
                 "Yoshi": "https://braacket.com/assets/images/game/ssbu/characters/yoshi.png",
                 "Kirby": "https://braacket.com/assets/images/game/ssbu/characters/kirby.png",
                 "Fox": "https://braacket.com/assets/images/game/ssbu/characters/fox.png",
                 "Pikachu": "https://braacket.com/assets/images/game/ssbu/characters/pikachu.png",
                 "Luigi": "https://braacket.com/assets/images/game/ssbu/characters/luigi.png",
                 "Ness": "https://braacket.com/assets/images/game/ssbu/characters/ness.png",
                 "Captain Falcon": "https://braacket.com/assets/images/game/ssbu/characters/captain_falcon.png",
                 "Jigglypuff": "https://braacket.com/assets/images/game/ssbu/characters/jigglypuff.png",
                 "Peach": "https://braacket.com/assets/images/game/ssbu/characters/peach.png",
                 "Daisy": "https://braacket.com/assets/images/game/ssbu/characters/daisy.png",
                 "Bowser": "https://braacket.com/assets/images/game/ssbu/characters/bowser.png",
                 "Ice Climbers": "https://braacket.com/assets/images/game/ssbu/characters/ice_climbers.png",
                 "Sheik": "https://braacket.com/assets/images/game/ssbu/characters/sheik.png",
                 "Zelda": "https://braacket.com/assets/images/game/ssbu/characters/zelda.png",
                 "Dr Mario": "https://braacket.com/assets/images/game/ssbu/characters/dr_mario.png",
                 "Pichu": "https://braacket.com/assets/images/game/ssbu/characters/pichu.png",
                 "Falco": "https://braacket.com/assets/images/game/ssbu/characters/falco.png",
                 "Marth": "https://braacket.com/assets/images/game/ssbu/characters/marth.png",
                 "Lucina": "https://braacket.com/assets/images/game/ssbu/characters/lucina.png",
                 "Young Link": "https://braacket.com/assets/images/game/ssbu/characters/young_link.png",
                 "Ganondorf": "https://braacket.com/assets/images/game/ssbu/characters/ganondorf.png",
                 "Mewtwo": "https://braacket.com/assets/images/game/ssbu/characters/mewtwo.png",
                 "Roy": "https://braacket.com/assets/images/game/ssbu/characters/roy.png",
                 "Chrom": "https://braacket.com/assets/images/game/ssbu/characters/chrom.png",
                 "Mr Game And Watch": "https://braacket.com/assets/images/game/ssbu/characters/mr_game_and_watch.png",
                 "Meta Knight": "https://braacket.com/assets/images/game/ssbu/characters/meta_knight.png",
                 "Pit": "https://braacket.com/assets/images/game/ssbu/characters/pit.png",
                 "Dark Pit": "https://braacket.com/assets/images/game/ssbu/characters/dark_pit.png",
                 "Zero Suit Samus": "https://braacket.com/assets/images/game/ssbu/characters/zero_suit_samus.png",
                 "Wario": "https://braacket.com/assets/images/game/ssbu/characters/wario.png",
                 "Snake": "https://braacket.com/assets/images/game/ssbu/characters/snake.png",
                 "Ike": "https://braacket.com/assets/images/game/ssbu/characters/ike.png",
                 "Pokemon Trainer": "https://braacket.com/assets/images/game/ssbu/characters/pokemon_trainer.png",
                 "Diddy Kong": "https://braacket.com/assets/images/game/ssbu/characters/diddy_kong.png",
                 "Lucas": "https://braacket.com/assets/images/game/ssbu/characters/lucas.png",
                 "Sonic": "https://braacket.com/assets/images/game/ssbu/characters/sonic.png",
                 "King Dedede": "https://braacket.com/assets/images/game/ssbu/characters/king_dedede.png",
                 "Olimar": "https://braacket.com/assets/images/game/ssbu/characters/olimar.png",
                 "Lucario": "https://braacket.com/assets/images/game/ssbu/characters/lucario.png",
                 "Rob": "https://braacket.com/assets/images/game/ssbu/characters/rob.png",
                 "Toon Link": "https://braacket.com/assets/images/game/ssbu/characters/toon_link.png",
                 "Wolf": "https://braacket.com/assets/images/game/ssbu/characters/wolf.png",
                 "Villager": "https://braacket.com/assets/images/game/ssbu/characters/villager.png",
                 "Mega Man": "https://braacket.com/assets/images/game/ssbu/characters/mega_man.png",
                 "Wii Fit Trainer":"https://braacket.com/assets/images/game/ssbu/characters/wii_fit_trainer.png",
                 "Rosalina And Luma": "https://braacket.com/assets/images/game/ssbu/characters/rosalina_and_luma.png",
                 "Little Mac": "https://braacket.com/assets/images/game/ssbu/characters/little_mac.png",
                 "Greninja": "https://braacket.com/assets/images/game/ssbu/characters/greninja.png",
                 "Mii Swordfighter": "https://braacket.com/assets/images/game/ssbu/characters/mii_swordfighter.png",
                 "Mii Brawler": "https://braacket.com/assets/images/game/ssbu/characters/mii_brawler.png",
                 "Mii Gunner": "https://braacket.com/assets/images/game/ssbu/characters/mii_gunner.png",
                 "Palutena": "https://braacket.com/assets/images/game/ssbu/characters/palutena.png",
                 "Pac Man": "https://braacket.com/assets/images/game/ssbu/characters/pac_man.png",
                 "Robin": "https://braacket.com/assets/images/game/ssbu/characters/robin.png",
                 "Shulk": "https://braacket.com/assets/images/game/ssbu/characters/shulk.png",
                 "Bowser Jr": "https://braacket.com/assets/images/game/ssbu/characters/bowser_jr.png",
                 "Duck Hunt": "https://braacket.com/assets/images/game/ssbu/characters/duck_hunt.png",
                 "Ryu": "https://braacket.com/assets/images/game/ssbu/characters/ryu.png",
                 "Ken": "https://braacket.com/assets/images/game/ssbu/characters/ken.png",
                 "Cloud": "https://braacket.com/assets/images/game/ssbu/characters/cloud.png",
                 "Corrin": "https://braacket.com/assets/images/game/ssbu/characters/corrin.png",
                 "Bayonetta": "https://braacket.com/assets/images/game/ssbu/characters/bayonetta.png",
                 "Inkling": "https://braacket.com/assets/images/game/ssbu/characters/inkling.png",
                 "Ridley": "https://braacket.com/assets/images/game/ssbu/characters/ridley.png",
                 "Simon": "https://braacket.com/assets/images/game/ssbu/characters/simon.png",
                 "Richter": "https://braacket.com/assets/images/game/ssbu/characters/richter.png",
                 "King K Rool": "https://braacket.com/assets/images/game/ssbu/characters/kingkrool.png",
                 "Isabelle": "https://braacket.com/assets/images/game/ssbu/characters/isabelle.png",
                 "Incineroar": "https://braacket.com/assets/images/game/ssbu/characters/incineroar.png",
                 "Piranha Plant": "https://braacket.com/assets/images/game/ssbu/characters/piranha_plant.png",
                 "Joker": "https://braacket.com/assets/images/game/ssbu/characters/joker.png",
                 "Hero": "https://braacket.com/assets/images/game/ssbu/characters/hero.png",
                 "Banjo-Kazooie": "https://braacket.com/assets/images/game/ssbu/characters/banjo-kazooie.png",
                 "Terry": "https://braacket.com/assets/images/game/ssbu/characters/terry.png",
                 "Byleth": "https://braacket.com/assets/images/game/ssbu/characters/byleth.png",
                 "Min Min": "https://braacket.com/assets/images/game/ssbu/characters/minmin.png",
                 "Steve": "https://braacket.com/assets/images/game/ssbu/characters/steve.png",
                 "Sephiroth": "https://braacket.com/assets/images/game/ssbu/characters/sephiroth.png",
                 "Pyra Mythra": "https://braacket.com/assets/images/game/ssbu/characters/pyramythra.png",
                 "Kazuya": "https://braacket.com/assets/images/game/ssbu/characters/kazuya.png",
                 "Sora": "https://braacket.com/assets/images/game/ssbu/characters/sora.png",
                 "Random": "https://braacket.com/assets/images/game/ssbu/characters/random.png"}
# Smash Bros Roster Images
ssbuRosterProfileImg = {"Mario": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dddzk16-416a9339-2324-4629-a838-aa55f141df16.png/v1/fit/w_828,h_1298/01_mario___super_smash_bros__ultimate_by_elevenzm_dddzk16-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjE2OCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRkemsxNi00MTZhOTMzOS0yMzI0LTQ2MjktYTgzOC1hYTU1ZjE0MWRmMTYucG5nIiwid2lkdGgiOiI8PTEzODIifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.KcP7FyDfaSf8ZuvffATGe3S6_g__qkxcirFFL4At6GM",
                   "Donkey Kong": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dddzlp6-a7d8c5a1-2487-46fb-958f-7e8bba658d79.png/v1/fill/w_913,h_875/02_donkey_kong___super_smash_bros__ultimate_by_elevenzm_dddzlp6-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTE0NyIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRkemxwNi1hN2Q4YzVhMS0yNDg3LTQ2ZmItOTU4Zi03ZThiYmE2NThkNzkucG5nIiwid2lkdGgiOiI8PTExOTYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.BwpHXV8kiF-ceFJa6AwD1Cc14knkPsXBbhFR7HLRswY",
                   "Link": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dddzlw7-aa55e596-c2be-44b3-b018-4b58d9a2ed7e.png/v1/fit/w_828,h_1098/03_link___super_smash_bros__ultimate_by_elevenzm_dddzlw7-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjYzMiIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRkemx3Ny1hYTU1ZTU5Ni1jMmJlLTQ0YjMtYjAxOC00YjU4ZDlhMmVkN2UucG5nIiwid2lkdGgiOiI8PTE5ODYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.U3u6eNiv57L3FPXTpnjL9fKSzH-xrFaOpyZkq5T-M4s",
                 "Samus": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dddzm2y-812bd8d4-36b1-4221-acd4-cbe84ca09f9d.png/v1/fill/w_835,h_957/04_samus___super_smash_bros__ultimate_by_elevenzm_dddzm2y-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTY0MSIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRkem0yeS04MTJiZDhkNC0zNmIxLTQyMjEtYWNkNC1jYmU4NGNhMDlmOWQucG5nIiwid2lkdGgiOiI8PTE0MzIifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.1gc0np3qFcFyMDuFkHWNfDbKMXcopsm-1qzk6acAY9M",
                 "Dark Samus": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dddzm75-9a785930-b809-4153-ab5f-3b48c7ff0791.png/v1/fit/w_828,h_1270/04e_dark_samus___super_smash_bros__ultimate_by_elevenzm_dddzm75-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTcwMCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRkem03NS05YTc4NTkzMC1iODA5LTQxNTMtYWI1Zi0zYjQ4YzdmZjA3OTEucG5nIiwid2lkdGgiOiI8PTExMDkifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.pEQHeFtGCpJYcAw_DaYHSST9NGCOUiUPHSNR6-MQcYI",
                 "Yoshi": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dddzmdc-ba514013-a8d5-406b-a31c-c813c2aac66b.png/v1/fill/w_909,h_880/05_yoshi___super_smash_bros__ultimate_by_elevenzm_dddzmdc-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI0MiIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRkem1kYy1iYTUxNDAxMy1hOGQ1LTQwNmItYTMxYy1jODEzYzJhYWM2NmIucG5nIiwid2lkdGgiOiI8PTEyODMifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.w56PIRbZAWw_gfQreDKfs5jDFgZdGOKvBRADsjLjiJY",
                 "Kirby": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dddzmqh-71632992-44f8-4a67-acbe-e371078d7e52.png/v1/fill/w_940,h_746/06_kirby___super_smash_bros__ultimate_by_elevenzm_dddzmqh-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NzQ2IiwicGF0aCI6IlwvZlwvOTgwODU1OTctMjQ4Yy00NWFkLWFjYjgtOTFiNzAwZDZmODg3XC9kZGR6bXFoLTcxNjMyOTkyLTQ0ZjgtNGE2Ny1hY2JlLWUzNzEwNzhkN2U1Mi5wbmciLCJ3aWR0aCI6Ijw9OTQwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.ZWL-dFoWDa45GR_WvXtRnAwykd3trQm_Qrtnx00G_2Y",
                 "Fox": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dddzmxk-a0e50b52-a434-4491-a265-e403f22d179c.png/v1/fill/w_849,h_941/07_fox___super_smash_bros__ultimate_by_elevenzm_dddzmxk-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjMzMyIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRkem14ay1hMGU1MGI1Mi1hNDM0LTQ0OTEtYTI2NS1lNDAzZjIyZDE3OWMucG5nIiwid2lkdGgiOiI8PTIxMDQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.-z_L8FqL8icITFxXbmxdGoqcu9Ogv-VvIuX3fSj9Y0g",
                 "Pikachu": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dddzn3k-d75f898f-3148-496e-90d3-f31b6e23e196.png/v1/fill/w_854,h_935/08_pikachu___super_smash_bros__ultimate_by_elevenzm_dddzn3k-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjE1MyIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRkem4zay1kNzVmODk4Zi0zMTQ4LTQ5NmUtOTBkMy1mMzFiNmUyM2UxOTYucG5nIiwid2lkdGgiOiI8PTE5NjcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.O85RD85MNyfphvdsvOnGR8YxnnceWFg6PJ2wkQUQvzg",
                 "Luigi": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddf1klr-d76e612d-fdc7-421d-9483-ec89dcd9f93b.png/v1/fill/w_864,h_353/luigi__no_smoke____super_smash_bros__ultimate_by_elevenzm_ddf1klr-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MzUzIiwicGF0aCI6IlwvZlwvOTgwODU1OTctMjQ4Yy00NWFkLWFjYjgtOTFiNzAwZDZmODg3XC9kZGYxa2xyLWQ3NmU2MTJkLWZkYzctNDIxZC05NDgzLWVjODlkY2Q5ZjkzYi5wbmciLCJ3aWR0aCI6Ijw9ODY0In1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.bgVu0swPOBsPzMTbKx4TWCoU5HU_3dCLYzUjUew4uas",
                 "Ness": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddf1psw-1b014794-d5f3-4fbf-aeed-2a96f0a251fe.png/v1/fill/w_904,h_884/10_ness__no_pk____super_smash_bros__ultimate_by_elevenzm_ddf1psw-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTE1OCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRmMXBzdy0xYjAxNDc5NC1kNWYzLTRmYmYtYWVlZC0yYTk2ZjBhMjUxZmUucG5nIiwid2lkdGgiOiI8PTExODQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.KBfl13LCv3RDpIguo8tkp2t608dDVPuwZyCiNQzNXiQ",
                 "Captain Falcon": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dddzonv-5058c34d-4933-4e87-8299-34a3a45cd19e.png/v1/fill/w_837,h_955/11_captain_falcon___super_smash_bros__ultimate_by_elevenzm_dddzonv-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTk0NCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRkem9udi01MDU4YzM0ZC00OTMzLTRlODctODI5OS0zNGEzYTQ1Y2QxOWUucG5nIiwid2lkdGgiOiI8PTE3MDQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.DcF_YgWtLt9hDEo1wDqXlAcN6FPm_XqKH9Ecw4X9htY",
                 "Jigglypuff": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dddzosf-99124c64-d80d-406c-b42d-a81e8f09bbed.png/v1/fit/w_571,h_628/12_jigglypuff___purin___super_smash_bros__ultimate_by_elevenzm_dddzosf-375w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NjI4IiwicGF0aCI6IlwvZlwvOTgwODU1OTctMjQ4Yy00NWFkLWFjYjgtOTFiNzAwZDZmODg3XC9kZGR6b3NmLTk5MTI0YzY0LWQ4MGQtNDA2Yy1iNDJkLWE4MWU4ZjA5YmJlZC5wbmciLCJ3aWR0aCI6Ijw9NTcxIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.-2IDrOLpq4W_Fc-xvQ0S7u4UTqt3czZ-zmPOYbW6Z9k",
                 "Peach": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde2f84-5f1fc50b-775f-47e5-b9b0-74ed36a43907.png/v1/fit/w_828,h_1144/13_peach___super_smash_bros__ultimate_by_elevenzm_dde2f84-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTQ5NCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlMmY4NC01ZjFmYzUwYi03NzVmLTQ3ZTUtYjliMC03NGVkMzZhNDM5MDcucG5nIiwid2lkdGgiOiI8PTEwODEifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.O4AjmZjWda1tVrZ6k40jN_UB-F9iLzEHY3UIBmW-LsI",
                 "Daisy": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dduh0ru-2a376e14-0d3e-43e2-b8e0-0864dfb69ee6.png/v1/fit/w_828,h_1130/13e_daisy___super_smash_bros__ultimate_by_elevenzm_dduh0ru-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTc0OCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGR1aDBydS0yYTM3NmUxNC0wZDNlLTQzZTItYjhlMC0wODY0ZGZiNjllZTYucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.MIO8ZFsEjoKzNh2hgnwPvBP4F45jLtbmoQ2RJ0RF2MA",
                 "Bowser": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde2fg1-0dc308ed-459c-417c-88e2-e2875fc13a30.png/v1/fill/w_853,h_937/14_bowser___koopa___super_smash_bros__ultimate_by_elevenzm_dde2fg1-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjI4NSIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlMmZnMS0wZGMzMDhlZC00NTljLTQxN2MtODhlMi1lMjg3NWZjMTNhMzAucG5nIiwid2lkdGgiOiI8PTIwODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.5KuTbA_0Xv3mvoDvE_Qu8UNeTqzzPlNhOCAfnPCOQYY",
                 "Ice Climbers": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde2flz-2ed0437d-9e9b-4be2-8cf1-84f05385adf8.png/v1/fit/w_828,h_1212/15_ice_climbers___super_smash_bros__ultimate_by_elevenzm_dde2flz-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjMyOSIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlMmZsei0yZWQwNDM3ZC05ZTliLTRiZTItOGNmMS04NGYwNTM4NWFkZjgucG5nIiwid2lkdGgiOiI8PTE1OTIifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.AVYCUlnJHQ0dM7G4FzglqByGs8uT92Xp9pTpS7Fong4",
                 "Sheik": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde2fqw-d998043e-fb96-4da4-a8df-966141ee8e9b.png/v1/fill/w_922,h_867/16_sheik___super_smash_bros__ultimate_by_elevenzm_dde2fqw-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTIzOSIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlMmZxdy1kOTk4MDQzZS1mYjk2LTRkYTQtYThkZi05NjYxNDFlZThlOWIucG5nIiwid2lkdGgiOiI8PTEzMTgifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.XZyCh8Z1zHoSEF_hH7qzSSe3ttFYKCv8HnnLHYW17XA",
                 "Zelda": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde2ftz-ac6566a9-aa96-43e2-8f43-7c6f48a4d3b5.png/v1/fit/w_828,h_1034/17_zelda___super_smash_bros__ultimate_by_elevenzm_dde2ftz-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTY5NSIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlMmZ0ei1hYzY1NjZhOS1hYTk2LTQzZTItOGY0My03YzZmNDhhNGQzYjUucG5nIiwid2lkdGgiOiI8PTEzNTcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.vuphmI_rN7I6NUlfSlJHmA3zw-7H-Eb2xIvGYEYdeLg",
                 "Dr Mario": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde2fxv-1669a7ef-77bf-4ecc-b56b-01acc86c446b.png/v1/fit/w_828,h_1212/18_dr__mario___super_smash_bros__ultimate_by_elevenzm_dde2fxv-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTM0NiIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlMmZ4di0xNjY5YTdlZi03N2JmLTRlY2MtYjU2Yi0wMWFjYzg2YzQ0NmIucG5nIiwid2lkdGgiOiI8PTkxOSJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.nTXOXDzP6wwym1gDft6VISDiIdveM6D2klqjzf-uvCo",
                 "Pichu": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde2g0t-88894a91-14bf-4422-bd97-fbc1ef8f6829.png/v1/fit/w_733,h_772/19_pichu___super_smash_bros__ultimate_by_elevenzm_dde2g0t-375w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NzcyIiwicGF0aCI6IlwvZlwvOTgwODU1OTctMjQ4Yy00NWFkLWFjYjgtOTFiNzAwZDZmODg3XC9kZGUyZzB0LTg4ODk0YTkxLTE0YmYtNDQyMi1iZDk3LWZiYzFlZjhmNjgyOS5wbmciLCJ3aWR0aCI6Ijw9NzMzIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.0PgpsQFMCgRAujY3dSBaByWDB9hTwDQ4wUJaHSUS4EI",
                 "Falco": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde2g4e-33e6ad1d-e901-457e-b00f-aebe374a6450.png/v1/fill/w_1099,h_727/20_falco___super_smash_bros__ultimate_by_elevenzm_dde2g4e-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9ODc1IiwicGF0aCI6IlwvZlwvOTgwODU1OTctMjQ4Yy00NWFkLWFjYjgtOTFiNzAwZDZmODg3XC9kZGUyZzRlLTMzZTZhZDFkLWU5MDEtNDU3ZS1iMDBmLWFlYmUzNzRhNjQ1MC5wbmciLCJ3aWR0aCI6Ijw9MTMyMiJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.9qgBUJFBvAv1Dd0kbk4i0bkXu1iIOkWDeywp9Co1Rhk",
                 "Marth": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde4j08-4242add0-f991-45e1-bf8d-e93b4a6dac2b.png/v1/fill/w_1027,h_778/21_marth___super_smash_bros__ultimate_by_elevenzm_dde4j08-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjEyMyIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlNGowOC00MjQyYWRkMC1mOTkxLTQ1ZTEtYmY4ZC1lOTNiNGE2ZGFjMmIucG5nIiwid2lkdGgiOiI8PTI4MDMifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.JuM-G4abguqJ2LAb5w79L-cL8KHPaOA_uzy76X5Cbo8",
                 "Lucina": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde4j5c-0eb203cd-63cd-4809-a5cf-46d7b3307286.png/v1/fill/w_965,h_828/21e_lucina___super_smash_bros__ultimate_by_elevenzm_dde4j5c-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTcxMCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlNGo1Yy0wZWIyMDNjZC02M2NkLTQ4MDktYTVjZi00NmQ3YjMzMDcyODYucG5nIiwid2lkdGgiOiI8PTE5OTQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.834425TpRv-fD3eDyDDgeDi4garmDc9B8oe2DphRPmk",
                 "Young Link": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde4j89-76fa4d4b-8fce-46b3-b43f-369cc51b02e3.png/v1/fit/w_769,h_1523/22_young_link___super_smash_bros__ultimate_by_elevenzm_dde4j89-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTUyMyIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlNGo4OS03NmZhNGQ0Yi04ZmNlLTQ2YjMtYjQzZi0zNjljYzUxYjAyZTMucG5nIiwid2lkdGgiOiI8PTc2OSJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.-PFiFxGCZ5a_WGvFyfrTxNB0b8tlKX3Gcgktrx4IA64",
                 "Ganondorf": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde4jbm-fd735840-4e0a-4ee4-ab37-c24ea9ec1ec1.png/v1/fill/w_843,h_948/23_ganondorf___super_smash_bros__ultimate_by_elevenzm_dde4jbm-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTY2OSIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlNGpibS1mZDczNTg0MC00ZTBhLTRlZTQtYWIzNy1jMjRlYTllYzFlYzEucG5nIiwid2lkdGgiOiI8PTE0ODQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.F72Ke7U9SqE-P9POP-c2evNVYqDZH3dSzrRW0PJQ68U",
                 "Mewtwo": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde4jef-d7b1d232-58cd-438e-8102-23056973e5c1.png/v1/fill/w_914,h_874/24_mewtwo___super_smash_bros__ultimate_by_elevenzm_dde4jef-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTM1NSIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlNGplZi1kN2IxZDIzMi01OGNkLTQzOGUtODEwMi0yMzA1Njk3M2U1YzEucG5nIiwid2lkdGgiOiI8PTE0MTYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.oDNkPSyyUMboAYZWl4IEp4IfSvbXGmARmhLdj7ZIqDM",
                 "Roy": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde4jjg-96d93092-fb49-418a-b0de-dd486c9f4629.png/v1/fill/w_838,h_953/25_roy___super_smash_bros__ultimate_by_elevenzm_dde4jjg-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjIxMiIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlNGpqZy05NmQ5MzA5Mi1mYjQ5LTQxOGEtYjBkZS1kZDQ4NmM5ZjQ2MjkucG5nIiwid2lkdGgiOiI8PTE5NDUifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.NWNAFYKfq4Vf4ZK0nPW-04C2c_aCTOmi8Ica9nY9EQ8",
                 "Chrom": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde4jnk-b469af9a-504e-4a05-b7ef-f59b40e31471.png/v1/fit/w_828,h_1152/25e_chrom___super_smash_bros__ultimate_by_elevenzm_dde4jnk-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjM1NSIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlNGpuay1iNDY5YWY5YS01MDRlLTRhMDUtYjdlZi1mNTliNDBlMzE0NzEucG5nIiwid2lkdGgiOiI8PTE2OTMifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.KSaqI5OjSvHJ-7puNBe9wo9YVGu3wMM7HrNs8upX6cs",
                 "Mr Game And Watch": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde4jqc-ac3f7ea3-0827-4fb6-a80a-b50e9002181f.png/v1/fit/w_785,h_1291/26_mr__game_and_watch___super_smash_bros__ultimate_by_elevenzm_dde4jqc-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI5MSIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlNGpxYy1hYzNmN2VhMy0wODI3LTRmYjYtYTgwYS1iNTBlOTAwMjE4MWYucG5nIiwid2lkdGgiOiI8PTc4NSJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.GhXlcZkeglDrO33eCMy0M_SBmB1npoC3xoxkJgzbONA",
                 "Meta Knight": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde70w8-629d68c3-0c2f-4301-ac7f-f2ad1df709ef.png/v1/fill/w_969,h_824/27_meta_knight___super_smash_bros__ultimate_by_elevenzm_dde70w8-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTM0MyIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlNzB3OC02MjlkNjhjMy0wYzJmLTQzMDEtYWM3Zi1mMmFkMWRmNzA5ZWYucG5nIiwid2lkdGgiOiI8PTE1NzkifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.FLqQ1JpCw8kGuv_3tj-Hvc09d6oVuGqezFuS_DEAIvk",
                 "Pit": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde7111-d6623106-7f78-4317-be89-d0bb02f7abfa.png/v1/fill/w_1223,h_653/28_pit___super_smash_bros__ultimate_by_elevenzm_dde7111-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9ODQ4IiwicGF0aCI6IlwvZlwvOTgwODU1OTctMjQ4Yy00NWFkLWFjYjgtOTFiNzAwZDZmODg3XC9kZGU3MTExLWQ2NjIzMTA2LTdmNzgtNDMxNy1iZTg5LWQwYmIwMmY3YWJmYS5wbmciLCJ3aWR0aCI6Ijw9MTU4NyJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.QVB6LBYfWDuRMQP0kKVcDf9QcvFBlPFnQUSqslZ-IN4",
                 "Dark Pit": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde7154-438f0d79-42fd-460f-9976-d710af6a2643.png/v1/fill/w_878,h_910/28e___dark_black_pit___super_smash_bros__ultimate_by_elevenzm_dde7154-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTIyMyIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlNzE1NC00MzhmMGQ3OS00MmZkLTQ2MGYtOTk3Ni1kNzEwYWY2YTI2NDMucG5nIiwid2lkdGgiOiI8PTExNzkifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.EubDQnNcJWSWxIcTqRrJNOh7_iwItHUjjWoT2sJOisA",
                 "Zero Suit Samus": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde71e4-4d7f0cb6-c5f6-4e6e-a4cb-71aba6eda97e.png/v1/fill/w_862,h_927/29_zero_suit_samus___super_smash_bros__ultimate_by_elevenzm_dde71e4-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTQwNyIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlNzFlNC00ZDdmMGNiNi1jNWY2LTRlNmUtYTRjYi03MWFiYTZlZGE5N2UucG5nIiwid2lkdGgiOiI8PTEzMDgifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.33ziTZUNiXa-lV5vzDQS4EUske_2zZQsTegk-4AkXzk",
                 "Wario": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde71iw-7abd7788-be8c-4542-a499-6f68fd96a363.png/v1/fill/w_947,h_844/30_wario___super_smash_bros__ultimate_by_elevenzm_dde71iw-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTU1OCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlNzFpdy03YWJkNzc4OC1iZThjLTQ1NDItYTQ5OS02ZjY4ZmQ5NmEzNjMucG5nIiwid2lkdGgiOiI8PTE3NDcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.SJ-xzi90yGNUPEqLeQzxHHTXz8bQjsNyl7GvziI8WRQ",
                 "Snake": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde71m4-f418e92a-5888-4871-89c0-777134b5a494.png/v1/fill/w_1030,h_776/31_snake___super_smash_bros__ultimate_by_elevenzm_dde71m4-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTUwOCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlNzFtNC1mNDE4ZTkyYS01ODg4LTQ4NzEtODljMC03NzcxMzRiNWE0OTQucG5nIiwid2lkdGgiOiI8PTIwMDEifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.kgwIBr4ZmQ6-iIJeh2qd-vBzyoGP4a1Ai79R1Y3Kjww",
                 "Ike": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde71pe-eed8084a-3da8-40ec-9eca-9d6d88a27031.png/v1/fit/w_828,h_1112/32_ike___super_smash_bros__ultimate_by_elevenzm_dde71pe-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjI3MCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlNzFwZS1lZWQ4MDg0YS0zZGE4LTQwZWMtOWVjYS05ZDZkODhhMjcwMzEucG5nIiwid2lkdGgiOiI8PTE2ODkifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.f9nKGQZyhlhAPZWfHbHU3IRsJdWPJJkRk8FRi58bSRg",
                 "Pokemon Trainer": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddf1r36-74bb132c-3ecb-4183-9e2c-039245935548.png/v1/fill/w_971,h_823/pkmn_trainer__with_pkmn____ssbu_by_elevenzm_ddf1r36-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjY3NyIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRmMXIzNi03NGJiMTMyYy0zZWNiLTQxODMtOWUyYy0wMzkyNDU5MzU1NDgucG5nIiwid2lkdGgiOiI8PTMxNTcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.m2EIjfD9XHy3UM2BNOFbRLplk0i9nQHJFIuU1KRy5iU",
                 "Diddy Kong": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddf1js1-15586ccb-1370-4038-91bb-3611f6b6329d.png/v1/fill/w_1047,h_739/36_diddy_kong__no_smoke____ssbu_by_elevenzm_ddf1js1-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NzM5IiwicGF0aCI6IlwvZlwvOTgwODU1OTctMjQ4Yy00NWFkLWFjYjgtOTFiNzAwZDZmODg3XC9kZGYxanMxLTE1NTg2Y2NiLTEzNzAtNDAzOC05MWJiLTM2MTFmNmI2MzI5ZC5wbmciLCJ3aWR0aCI6Ijw9MTA0NyJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.jG3AfSzsA0vzA7rc34VBI51pq0-tRW-1TXZ0V8UTZdM",
                 "Lucas": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde72h3-6b4245f8-2892-4549-8b98-84ebe8b8e93b.png/v1/fit/w_828,h_1074/37_lucas___super_smash_bros__ultimate_by_elevenzm_dde72h3-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjY2OCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlNzJoMy02YjQyNDVmOC0yODkyLTQ1NDktOGI5OC04NGViZThiOGU5M2IucG5nIiwid2lkdGgiOiI8PTIwNTYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.PNUHwe4jinhP8HePNehaus8gtTm0lFiDdDjxXWBfWSg",
                 "Sonic": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde72ml-9649599c-a945-4c9c-a65a-9033d43abf2d.png/v1/fill/w_926,h_863/38_sonic___super_smash_bros__ultimate_by_elevenzm_dde72ml-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTE5NCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlNzJtbC05NjQ5NTk5Yy1hOTQ1LTRjOWMtYTY1YS05MDMzZDQzYWJmMmQucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.oX8TyP8hF_sEiekocnUQ7tWBr4qRg88UfBwl5Yy3ttM",
                 "King Dedede": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde72ql-cf40add6-ee9f-48ec-9585-26c5de967d2a.png/v1/fill/w_970,h_824/39___king_dedede___super_smash_bros__ultimate_by_elevenzm_dde72ql-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTkzMyIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlNzJxbC1jZjQwYWRkNi1lZTlmLTQ4ZWMtOTU4NS0yNmM1ZGU5NjdkMmEucG5nIiwid2lkdGgiOiI8PTIyNzcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.PTWovzmzXqmtlD3QZ2nxBFXeJD5lZglzhv3io-2vMuI",
                 "Olimar": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddf1pve-5341cbc9-123e-4135-8d4e-5c2e2fe27e77.png/v1/fit/w_793,h_894/40_olimar__no_pikmin____super_smash_bros__ultimate_by_elevenzm_ddf1pve-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9ODk0IiwicGF0aCI6IlwvZlwvOTgwODU1OTctMjQ4Yy00NWFkLWFjYjgtOTFiNzAwZDZmODg3XC9kZGYxcHZlLTUzNDFjYmM5LTEyM2UtNDEzNS04ZDRlLTVjMmUyZmUyN2U3Ny5wbmciLCJ3aWR0aCI6Ijw9NzkzIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.6iAADjbwigPUEPvGnj5BfvNzeeEPBMn8RctmT4uij4g",
                 "Lucario": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde72zu-76c0c66e-a1ad-4dfd-a352-a843ef4585c1.png/v1/fit/w_828,h_1010/41_lucario___super_smash_bros__ultimate_by_elevenzm_dde72zu-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTQzOCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlNzJ6dS03NmMwYzY2ZS1hMWFkLTRkZmQtYTM1Mi1hODQzZWY0NTg1YzEucG5nIiwid2lkdGgiOiI8PTExNzgifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.VXNZxTVduELs0PlBqgAW_-fxzwpvk1-m35fv6UtWWDc",
                 "Rob": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde7369-8b2a60c2-4a69-4df3-a9ac-816bd2ad3efe.png/v1/fit/w_700,h_505/42_r_o_b____super_smash_bros__ultimate_by_elevenzm_dde7369-375w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTA1IiwicGF0aCI6IlwvZlwvOTgwODU1OTctMjQ4Yy00NWFkLWFjYjgtOTFiNzAwZDZmODg3XC9kZGU3MzY5LThiMmE2MGMyLTRhNjktNGRmMy1hOWFjLTgxNmJkMmFkM2VmZS5wbmciLCJ3aWR0aCI6Ijw9NzAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.k28IpqrjiO9QtQhRgNgXlrmaoXffW9-41RJTKnQ4mzc",
                 "Toon Link": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde739f-e064b1cb-4500-42f0-bd3f-d5676a22b9e8.png/v1/fill/w_893,h_895/43_toon_link___super_smash_bros__ultimate_by_elevenzm_dde739f-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTA5OSIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlNzM5Zi1lMDY0YjFjYi00NTAwLTQyZjAtYmQzZi1kNTY3NmEyMmI5ZTgucG5nIiwid2lkdGgiOiI8PTEwOTcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.ZaDL8KgN8Gz92Je_1kvEtlHsIMPwJ5IMyhU68wp3vxo",
                 "Wolf": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dde73cf-596a9b4a-b489-4b88-8d6e-57cb7eea3ea5.png/v1/fit/w_828,h_1020/44_wolf___super_smash_bros__ultimate_by_elevenzm_dde73cf-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTU3NyIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlNzNjZi01OTZhOWI0YS1iNDg5LTRiODgtOGQ2ZS01N2NiN2VlYTNlYTUucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.hCii_fm1sGD5Bx8l9dNTK5yWkGZyV7lBJZ01zLmj_IM",
                 "Villager": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddejooo-ff5aeec8-ec6a-4ad8-9916-b2690fda0b6f.png/v1/fill/w_1021,h_783/45_villager_murabito___super_smash_bros__ultimate_by_elevenzm_ddejooo-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTExMiIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlam9vby1mZjVhZWVjOC1lYzZhLTRhZDgtOTkxNi1iMjY5MGZkYTBiNmYucG5nIiwid2lkdGgiOiI8PTE0NTAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.dInG5LfKWlrHYxKUcAgeok3RzrtjHJxfw9DpRnntpgE",
                 "Mega Man": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddejow1-9570a5d8-2e3b-47cf-af44-99687cd70a86.png/v1/fill/w_1020,h_783/46_mega_man___rockman___super_smash_bros__ultimate_by_elevenzm_ddejow1-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTQzNCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlam93MS05NTcwYTVkOC0yZTNiLTQ3Y2YtYWY0NC05OTY4N2NkNzBhODYucG5nIiwid2lkdGgiOiI8PTE4NjgifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.QKJxZDX_DJi052l8DssTAtOL1medcPwvjNN8nZv82kE",
                 "Wii Fit Trainer":"https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddkoqkf-318c972f-a4d4-447f-9516-3506a3ea1995.png/v1/fit/w_508,h_1800/47_wii_fit_trainer__patched____ssbu_by_elevenzm_ddkoqkf-375w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NDYxNiIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRrb3FrZi0zMThjOTcyZi1hNGQ0LTQ0N2YtOTUxNi0zNTA2YTNlYTE5OTUucG5nIiwid2lkdGgiOiI8PTEzMDQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.V1DOUtuYpxR25rgJfx-PFqHeG_aYswoJYYGC_ZnxUVM",
                 "Rosalina And Luma": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddejp2z-5911cae8-425f-49b1-a36a-a84f759ba986.png/v1/fill/w_956,h_836/48_rosalina___rosetta___super_smash_bros__ultimate_by_elevenzm_ddejp2z-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTQ1MyIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlanAyei01OTExY2FlOC00MjVmLTQ5YjEtYTM2YS1hODRmNzU5YmE5ODYucG5nIiwid2lkdGgiOiI8PTE2NjEifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.wBti8tPvRDLY4FvhIJWo5D4rQyFOwr49CknyPg_QcIE",
                 "Little Mac": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddejp6z-8d6176ce-eba8-45e9-b138-394a370b178b.png/v1/fit/w_828,h_1260/49_little_mac___super_smash_bros__ultimate_by_elevenzm_ddejp6z-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTQ5MiIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlanA2ei04ZDYxNzZjZS1lYmE4LTQ1ZTktYjEzOC0zOTRhMzcwYjE3OGIucG5nIiwid2lkdGgiOiI8PTk4MSJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.lXr1vf13YPQLQXiPXBoaqBD2pAke6TkVfdgubi8OW78",
                 "Greninja": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddejp97-3892db46-6cfb-40bd-8b31-e3f7e08631d9.png/v1/fill/w_1040,h_768/50_greninja_gekkouga___super_smash_bros__ultimate_by_elevenzm_ddejp97-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTE5MCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlanA5Ny0zODkyZGI0Ni02Y2ZiLTQwYmQtOGIzMS1lM2Y3ZTA4NjMxZDkucG5nIiwid2lkdGgiOiI8PTE2MTEifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.LK7FUasxwLnk_38DyQVv2gERINd3x1-1IYgYDPp7HTw",
                 "Mii Swordfighter": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddemd2p-929aeb45-d04f-4872-acd5-e8be4abf6e8f.png/v1/fill/w_955,h_680/52_mii_swordfighter___super_smash_bros__ultimate_by_elevenzm_ddemd2p-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NjgwIiwicGF0aCI6IlwvZlwvOTgwODU1OTctMjQ4Yy00NWFkLWFjYjgtOTFiNzAwZDZmODg3XC9kZGVtZDJwLTkyOWFlYjQ1LWQwNGYtNDg3Mi1hY2Q1LWU4YmU0YWJmNmU4Zi5wbmciLCJ3aWR0aCI6Ijw9OTU1In1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.O1P5-mra1acxEP6NGiRxyYf8XPVWbH3KGIRAtlnJJ_s",
                 "Mii Brawler": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddemcz1-be32e9b2-ad61-47e2-a9fb-a1e68c6af7b6.png/v1/fill/w_980,h_654/51_mii_brawler___super_smash_bros__ultimate_by_elevenzm_ddemcz1-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NjU0IiwicGF0aCI6IlwvZlwvOTgwODU1OTctMjQ4Yy00NWFkLWFjYjgtOTFiNzAwZDZmODg3XC9kZGVtY3oxLWJlMzJlOWIyLWFkNjEtNDdlMi1hOWZiLWExZTY4YzZhZjdiNi5wbmciLCJ3aWR0aCI6Ijw9OTgwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.2-Huwqkogxau6FYNEZbKDboIxe-ec4SMAxffeeBgqxA",
                 "Mii Gunner": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddemd76-778388a6-299f-43e8-af04-f0462759a13e.png/v1/fit/w_803,h_780/53_mii_gunner___super_smash_bros__ultimate_by_elevenzm_ddemd76-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NzgwIiwicGF0aCI6IlwvZlwvOTgwODU1OTctMjQ4Yy00NWFkLWFjYjgtOTFiNzAwZDZmODg3XC9kZGVtZDc2LTc3ODM4OGE2LTI5OWYtNDNlOC1hZjA0LWYwNDYyNzU5YTEzZS5wbmciLCJ3aWR0aCI6Ijw9ODAzIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.aC0vPKJjWXWAx_UfX2JnI4lX42pif0Haqpjn2R-eUpM",
                 "Palutena": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/de5fgnb-9c8d7e6b-59ec-44a9-9ea9-d73a84968123.png/v1/fill/w_845,h_945/54_palutena___super_smash_bros__ultimate_by_elevenzm_de5fgnb-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjMwNCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGU1ZmduYi05YzhkN2U2Yi01OWVjLTQ0YTktOWVhOS1kNzNhODQ5NjgxMjMucG5nIiwid2lkdGgiOiI8PTIwNjAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.kmBCN-7ENleTktpFF7x0raA3SbSpPn5uOBQ99FQ3CPY",
                 "Pac Man": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddemea9-d3699491-6f11-4cec-bdc6-07232be8dbcc.png/v1/fit/w_828,h_1146/55_pac_man___super_smash_bros__ultimate_by_elevenzm_ddemea9-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTM5NiIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlbWVhOS1kMzY5OTQ5MS02ZjExLTRjZWMtYmRjNi0wNzIzMmJlOGRiY2MucG5nIiwid2lkdGgiOiI8PTEwMDkifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.jvkaMxvf9fJGjSry2EiWXuNzvpyBD_KSeJrZGY6tEso",
                 "Robin": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddemedr-46f5528b-74e6-4df7-be41-72968823bdb0.png/v1/fill/w_908,h_880/56_robin___reflet___super_smash_bros__ultimate_by_elevenzm_ddemedr-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTExMiIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlbWVkci00NmY1NTI4Yi03NGU2LTRkZjctYmU0MS03Mjk2ODgyM2JkYjAucG5nIiwid2lkdGgiOiI8PTExNDgifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.SAksyV8mZgj370dFIU-A4ngO8bJxJ2dKB02AklQrHxs",
                 "Shulk": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddemejq-0b1ff85d-590d-4c73-840d-5dca992a8315.png/v1/fit/w_828,h_1468/57_shulk___super_smash_bros__ultimate_by_elevenzm_ddemejq-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTk0NyIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlbWVqcS0wYjFmZjg1ZC01OTBkLTRjNzMtODQwZC01ZGNhOTkyYTgzMTUucG5nIiwid2lkdGgiOiI8PTEwOTgifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.6HwA6kAKgulHBUV5n1RedAtKp98evJea-iqEYywjRsg",
                 "Bowser Jr": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddemeox-05ed26b8-6785-4381-bc8b-6748ee312f6c.png/v1/fit/w_659,h_699/58_bowser_koopa_jr____super_smash_bros__ultimate_by_elevenzm_ddemeox-375w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9Njk5IiwicGF0aCI6IlwvZlwvOTgwODU1OTctMjQ4Yy00NWFkLWFjYjgtOTFiNzAwZDZmODg3XC9kZGVtZW94LTA1ZWQyNmI4LTY3ODUtNDM4MS1iYzhiLTY3NDhlZTMxMmY2Yy5wbmciLCJ3aWR0aCI6Ijw9NjU5In1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.0XPQTUuLUHzACOn8XeRxHRLz9mp29P3jW_M63YuVFss",
                 "Duck Hunt": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddemet0-046cbbbc-d6ca-4314-86f8-19c5241a425b.png/v1/fit/w_743,h_1482/59_duck_hunt___duo___super_smash_bros__ultimate_by_elevenzm_ddemet0-375w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTQ4MiIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlbWV0MC0wNDZjYmJiYy1kNmNhLTQzMTQtODZmOC0xOWM1MjQxYTQyNWIucG5nIiwid2lkdGgiOiI8PTc0MyJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19._w4ZsWFSjdEcRi0BM1XOyS3uSK04QX4hoDM3FZ0kNTY",
                 "Ryu": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddemf1t-e0157499-4ce0-4787-8ee1-f69038449776.png/v1/fill/w_903,h_885/60_ryu___super_smash_bros__ultimate_by_elevenzm_ddemf1t-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTgwNCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlbWYxdC1lMDE1NzQ5OS00Y2UwLTQ3ODctOGVlMS1mNjkwMzg0NDk3NzYucG5nIiwid2lkdGgiOiI8PTE4NDEifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.7I0J6mzZzBtGcGOaq-OrU4RFuFsLQdTMiZT2Y3bVjTw",
                 "Ken": "https://cdn.discordapp.com/attachments/1277272930451198067/1277322860016304218/ken.png?ex=66ccbf1d&is=66cb6d9d&hm=739cb81e2fb11ff1195b55a70eee872a180bdf0aee66a1d3e8e99804dd2a9252&",
                 "Cloud": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddemfds-581ce2aa-853d-49fe-aceb-45a56070de99.png/v1/fill/w_1032,h_774/61_cloud___super_smash_bros__ultimate_by_elevenzm_ddemfds-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTkzMCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlbWZkcy01ODFjZTJhYS04NTNkLTQ5ZmUtYWNlYi00NWE1NjA3MGRlOTkucG5nIiwid2lkdGgiOiI8PTI1NzQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.B07kcO7zG38JhvXxfsQMbURZ3g3F49NwnUJ9u0K-tb4",
                 "Corrin": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddemflq-210c5fb3-e92e-4ed3-8bb6-2aecdca86a77.png/v1/fill/w_896,h_892/62_corrin___kamui___super_smash_bros__ultimate_by_elevenzm_ddemflq-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTc3MCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlbWZscS0yMTBjNWZiMy1lOTJlLTRlZDMtOGJiNi0yYWVjZGNhODZhNzcucG5nIiwid2lkdGgiOiI8PTE3NzcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.SZSYWRgoJghzOhow7V4AynGoM1XzdAo6Oxjx6CagxWY",
                 "Bayonetta": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddemg4n-b9f91baa-d666-40da-ae94-f463bcf868f6.png/v1/fill/w_933,h_857/63_bayonetta___super_smash_bros__ultimate_by_elevenzm_ddemg4n-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTk2NiIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRlbWc0bi1iOWY5MWJhYS1kNjY2LTQwZGEtYWU5NC1mNDYzYmNmODY4ZjYucG5nIiwid2lkdGgiOiI8PTIxNDEifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.LpaTs8yGMRkKhCjkZ_1fqajV5Y2AM8363NejJlggyuI",
                 "Inkling": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddeyswg-13cd22bf-8b0e-4514-a6ec-0fd815c5a6d0.png/v1/fill/w_961,h_831/64_inkling___super_smash_bros__ultimate_by_elevenzm_ddeyswg-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTg0MiIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRleXN3Zy0xM2NkMjJiZi04YjBlLTQ1MTQtYTZlYy0wZmQ4MTVjNWE2ZDAucG5nIiwid2lkdGgiOiI8PTIxMjkifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.pe29QB_1pWkXj4Ou_DmoeWiC1YPP3S9PVywQyrXa1aw",
                 "Ridley": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddeyt0w-56a8c7c7-3f35-4aef-ab02-ad4083888d01.png/v1/fill/w_944,h_846/65_ridley___super_smash_bros__ultimate_by_elevenzm_ddeyt0w-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTcwMyIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRleXQwdy01NmE4YzdjNy0zZjM1LTRhZWYtYWIwMi1hZDQwODM4ODhkMDEucG5nIiwid2lkdGgiOiI8PTE5MDAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.YXi8kxIzC3GWxSJN-rngZrb10iGsUEmcQxcxQIMtslA",
                 "Simon": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/de5yk4z-c8e08c21-a734-47e0-b6ca-440822e12c40.png/v1/fit/w_828,h_1020/66_simon___super_smash_bros__ultimate_by_elevenzm_de5yk4z-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9Mjc1NiIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGU1eWs0ei1jOGUwOGMyMS1hNzM0LTQ3ZTAtYjZjYS00NDA4MjJlMTJjNDAucG5nIiwid2lkdGgiOiI8PTIyMzcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.ax4yvx7iI9fJj43BcInBUF_JftaaXjzQPq7xG_JPVhg",
                 "Richter": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddeyt97-07c694a4-7d3b-4496-bdca-1fa4aba81c68.png/v1/fit/w_828,h_994/66e_richter___super_smash_bros__ultimate_by_elevenzm_ddeyt97-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjUyMyIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRleXQ5Ny0wN2M2OTRhNC03ZDNiLTQ0OTYtYmRjYS0xZmE0YWJhODFjNjgucG5nIiwid2lkdGgiOiI8PTIxMDAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.kJ2vN7yINw-GagZUtovVYbgo60-Fy2teVG_igGofRP0",
                 "King K Rool": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dduh0z0-b1dbced5-987a-49de-961e-44006ad87e07.png/v1/fit/w_828,h_1020/67_king_k__rool___super_smash_bros__ultimate_by_elevenzm_dduh0z0-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjUwNCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGR1aDB6MC1iMWRiY2VkNS05ODdhLTQ5ZGUtOTYxZS00NDAwNmFkODdlMDcucG5nIiwid2lkdGgiOiI8PTIwMzMifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.n5lavSuX6fMrFkTztV1f6_74clbq8cHG3q2VNZGCvd0",
                 "Isabelle": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddeyti1-da598662-c8ef-4c88-aa8d-589716e48e1f.png/v1/fit/w_828,h_1112/68_isabelle___shizue___super_smash_bros__ultimate_by_elevenzm_ddeyti1-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTg1NCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRleXRpMS1kYTU5ODY2Mi1jOGVmLTRjODgtYWE4ZC01ODk3MTZlNDhlMWYucG5nIiwid2lkdGgiOiI8PTEzODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.UgwkawUEB3bo31sGj01Gfa6bqfxMDmJMIoYvIGErvB0",
                 "Incineroar": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddeyu9z-a35809d0-c0e1-4fce-940c-865dd4a3f891.png/v1/fill/w_902,h_886/69_incineroar_gaogaen___super_smash_bros__ultimate_by_elevenzm_ddeyu9z-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjI1NCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRleXU5ei1hMzU4MDlkMC1jMGUxLTRmY2UtOTQwYy04NjVkZDRhM2Y4OTEucG5nIiwid2lkdGgiOiI8PTIyOTQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.VsRm2C4IVxRrt1ezj4ZBAETn0fyvllD3BVHUsnr4l1E",
                 "Piranha Plant": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/de5ftko-e0fa8855-27e2-44c1-a8e6-f40aa873ebfd.png/v1/fit/w_828,h_996/70_piranha_plant___packun_flower___ssbu_by_elevenzm_de5ftko-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTgzMSIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGU1ZnRrby1lMGZhODg1NS0yN2UyLTQ0YzEtYThlNi1mNDBhYTg3M2ViZmQucG5nIiwid2lkdGgiOiI8PTE1MjMifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.C47gYZCdKoKZFrYo4dU_dfuxYCruFZzjyXfrZ1_8eb4",
                 "Joker": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/de5fn38-ca878e17-6e23-45cd-99e6-e422bc42f563.png/v1/fill/w_903,h_885/71_joker__alone____super_smash_bros__ultimate_by_elevenzm_de5fn38-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTcwOCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGU1Zm4zOC1jYTg3OGUxNy02ZTIzLTQ1Y2QtOTllNi1lNDIyYmM0MmY1NjMucG5nIiwid2lkdGgiOiI8PTE3NDMifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.opviFfWTSw-z1OPgHMw6oG0b4paAHlPAFBvNf9J4jZc",
                 "Hero": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/ddfx6uw-938dd05c-3609-485c-92a3-292bebf226ca.png/v1/fit/w_828,h_1024/72_hero___super_smash_bros__ultimate_by_elevenzm_ddfx6uw-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjA3MCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGRmeDZ1dy05MzhkZDA1Yy0zNjA5LTQ4NWMtOTJhMy0yOTJiZWJmMjI2Y2EucG5nIiwid2lkdGgiOiI8PTE2NzUifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.QXqfmrFMF8W_DuNi5eCdCjOIEqmrtkJMURIJzIicFok",
                 "Banjo-Kazooie": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/de5f8tf-926d99e6-7294-4e6c-b91a-a94d88d03aab.png/v1/fill/w_892,h_896/73_banjo_and_kazooie___super_smash_bros__ultimate_by_elevenzm_de5f8tf-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjAwNCIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGU1Zjh0Zi05MjZkOTllNi03Mjk0LTRlNmMtYjkxYS1hOTRkODhkMDNhYWIucG5nIiwid2lkdGgiOiI8PTE5OTQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.OycS5ZwEyL8rRQISur6VLEtMcKfGyLV6NCV3as7IUaI",
                 "Terry": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/de40hfo-15de9115-2fc0-469f-841e-97eb05878786.png/v1/fit/w_828,h_1650/74_terry__new____super_smash_bros__ultimate_by_elevenzm_de40hfo-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjM2MyIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGU0MGhmby0xNWRlOTExNS0yZmMwLTQ2OWYtODQxZS05N2ViMDU4Nzg3ODYucG5nIiwid2lkdGgiOiI8PTExODYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.OpGf11l1PqbQgvFpKoAZSUWgaJuQ4oXKIpPkN1Oo1RY",
                 "Byleth": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/de626hd-2ccc371d-b248-4cfb-bb16-ebf46ec633b0.png/v1/fit/w_828,h_1608/75_byleth___super_smash_bros__ultimate_by_elevenzm_de626hd-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9Mjc5OSIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGU2MjZoZC0yY2NjMzcxZC1iMjQ4LTRjZmItYmIxNi1lYmY0NmVjNjMzYjAucG5nIiwid2lkdGgiOiI8PTE0NDEifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.a4eMi6MNFE1IdMYy-rhaGU0VaF_5roRVjWd9FH6qSIs",
                 "Min Min": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/de40hjz-70452977-6315-4f61-9cc3-9325036c6bd4.png/v1/fill/w_1228,h_651/76_min_min__patched____super_smash_bros__ultimate_by_elevenzm_de40hjz-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjAwNiIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGU0MGhqei03MDQ1Mjk3Ny02MzE1LTRmNjEtOWNjMy05MzI1MDM2YzZiZDQucG5nIiwid2lkdGgiOiI8PTM3ODYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.X7finSNvI6T3rTTgtpNtQJJeBzI5nmw4NXaJtE0MB40",
                 "Steve": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/de63jqv-5d2cb23a-9950-4ae9-a431-582d8448ff23.png/v1/fill/w_989,h_808/77_steve___super_smash_bros__ultimate_by_elevenzm_de63jqv-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTA3MSIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGU2M2pxdi01ZDJjYjIzYS05OTUwLTRhZTktYTQzMS01ODJkODQ0OGZmMjMucG5nIiwid2lkdGgiOiI8PTEzMTAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.sEgzPQX0GAJRa_6_Pbx5tg4zvYdMu6P9dgiCI_EN5Mc",
                 "Sephiroth": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/dea9pvq-82b29b3c-74a3-4729-9b40-8b907a4a1f5a.png/v1/fit/w_750,h_1800/78_sephiroth___super_smash_bros__ultimate_by_elevenzm_dea9pvq-375w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MzcwOSIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGVhOXB2cS04MmIyOWIzYy03NGEzLTQ3MjktOWI0MC04YjkwN2E0YTFmNWEucG5nIiwid2lkdGgiOiI8PTE1NDUifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.b5INKjv15IzyD5IDTVFBAfjVxuNkH14QiFj6t6S6LVg",
                 "Pyra Mythra": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/deehoux-f68a071d-4392-4ccf-a078-9ad0afb2a526.png/v1/fill/w_916,h_873/79_80_pyra_and_mythra___homura_hikari__ne__ssbu_by_elevenzm_deehoux-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjIxNyIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGVlaG91eC1mNjhhMDcxZC00MzkyLTRjY2YtYTA3OC05YWQwYWZiMmE1MjYucG5nIiwid2lkdGgiOiI8PTIzMjYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.WGLghqMARSoOD-aerMZesjALqYtRqGK77pXzntInj1Q",
                 "Kazuya": "https://cdn.discordapp.com/attachments/858162778341900288/1277325702953435136/kazuyapng.png?ex=66ccc1c3&is=66cb7043&hm=40cef5cbc9236b1c552ec9181ccb566b3b676b99e88e48171b585ff14a822bf4&",
                 "Sora": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/98085597-248c-45ad-acb8-91b700d6f887/des92t0-d80638fc-b5aa-4580-80b7-f530d0902230.png/v1/fill/w_854,h_935/82_sora___super_smash_bros__ultimate_by_elevenzm_des92t0-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTc4MSIsInBhdGgiOiJcL2ZcLzk4MDg1NTk3LTI0OGMtNDVhZC1hY2I4LTkxYjcwMGQ2Zjg4N1wvZGVzOTJ0MC1kODA2MzhmYy1iNWFhLTQ1ODAtODBiNy1mNTMwZDA5MDIyMzAucG5nIiwid2lkdGgiOiI8PTE2MjcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.3on6zkTlvR01pSjSsDHkU05Q158TBNHJF9VoczwCxP0",
                 "Random": "https://streameta.com/images/characters/SSBU/portraits/random-1.png"}
# Yet another dictionary. Smash Bros Roster Emojis
ssbuRosterEmojis = {"Mario": "<:mario:1277311818628337745>",
                 "Donkey Kong": "<:donkey_kong:1277310685868589126>",
                 "Link": "<:link:1277311709069181021>",
                 "Samus": "<:samus:1277312387107655753>",
                 "Dark Samus": "<:darksamus:1277310655916937266>",
                 "Yoshi": "<:yoshi:1277312709884514324>",
                 "Kirby": "<:kirby:1277311691436195850>",
                 "Fox": "<:fox:1277310730470821948>",
                 "Pikachu": "<:pikachu:1277312098329825420>",
                 "Luigi": "<:luigi:1277311804359442524>",
                 "Ness": "<:ness:1277312006784946238>",
                 "Captain Falcon": "<:captain_falcon:1277310580138578010>",
                 "Jigglypuff": "<:jigglypuff:1277310891074912349>",
                 "Peach": "<:peach:1277312072333660265>",
                 "Daisy": "<:daisy:1277310626514997340>",
                 "Bowser": "<:bowser:1277310529819639848>",
                 "Ice Climbers": "<:ice_climbers:1277310800553312337>",
                 "Sheik": "<:sheik:1277312422927007865>",
                 "Zelda": "<:zelda:1277312744588054608>",
                 "Dr Mario": "<:dr_mario:1277310698501832847>",
                 "Pichu": "<:pichu:1277312085755301970>",
                 "Falco": "<:falco:1277310719859359754>",
                 "Marth": "<:marth:1277311831878271059>",
                 "Lucina": "<:lucina:1277311788878397441>",
                 "Young Link": "<:young_link:1277312726854799400>",
                 "Ganondorf": "<:ganondorf:1277310740922896405>",
                 "Mewtwo": "<:mewtwo:1277311878959206430>",
                 "Roy": "<:roy:1277312348201160808>",
                 "Chrom": "<:chrom:1277310591525978122>",
                 "Mr Game And Watch": "<:mr_game_and_watch:1277311973180182629>",
                 "Meta Knight": "<:meta_knight:1277311860357595191>",
                 "Pit": "<:pit:1277312179934330955>",
                 "Dark Pit": "<:dark_pit:1277310638971945030>",
                 "Zero Suit Samus": "<:zero_suit_samus:1277312758106292234>",
                 "Wario": "<:wario:1277312660136005692>",
                 "Snake": "<:snake:1277312501104513145>",
                 "Ike": "<:ike:1277310813484351540>",
                 "Pokemon Trainer": "<:pokemon_trainer:1277312199735640115>",
                 "Diddy Kong": "<:diddy_kong:1277310673138749531>",
                 "Lucas": "<:lucas:1277311771601932288>",
                 "Sonic": "<:sonic:1277312518741823539>",
                 "King Dedede": "<:king_dedede:1277311643528859732>",
                 "Olimar": "<:olimar:1277312023021228147>",
                 "Lucario": "<:lucario:1277311758498791545>",
                 "Rob": "<:rob:1277312290546516058>",
                 "Toon Link": "<:toon_link:1277312582855954494>",
                 "Wolf": "<:wolf:1277312692981600359>",
                 "Villager": "<:villager:1277312601197645947>",
                 "Mega Man": "<:mega_man:1277311844851388517>",
                 "Wii Fit Trainer":"<:wii_fit_trainer:1277312675306672231>",
                 "Rosalina And Luma": "<:rosalina_and_luma:1277312328706293810>",
                 "Little Mac": "<:little_mac:1277311722696212633>",
                 "Greninja": "<:greninja:1277310751350198500>",
                 "Mii Swordfighter": "<:mii_swordfighter:1277311940468674570>",
                 "Mii Brawler": "<:mii_brawler:1277311896894308403>",
                 "Mii Gunner": "<:mii_gunner:1277311914875158548>",
                 "Palutena": "<:palutena:1277312058941247579>",
                 "Pac Man": "<:pac_man:1277312040071069896>",
                 "Robin": "<:robin:1277312306325229640>",
                 "Shulk": "<:shulk:1277312465524228106>",
                 "Bowser Jr": "<:bowser_jr:1277360061559210024>",
                 "Duck Hunt": "<:duck_hunt:1277310708601847970>",
                 "Ryu": "<:ryu:1277312368170369186>",
                 "Ken": "<:ken:1277311627099901992>",
                 "Cloud": "<:cloud:1277310603232280689>",
                 "Corrin": "<:corrin:1277310614842118287>",
                 "Bayonetta": "<:bayonetta:1277310511821881355>",
                 "Inkling": "<:inkling:1277310854592987260>",
                 "Ridley": "<:ridley:1277312271026229351>",
                 "Simon": "<:simon:1277312484642132039>",
                 "Richter": "<:richter:1277312253497966662>",
                 "King K Rool": "<:kingkrool:1277311675648708608>",
                 "Isabelle": "<:isabelle:1277310872603201586>",
                 "Incineroar": "<:incineroar:1277310830152777748>",
                 "Piranha Plant": "<:piranha_plant:1277312165862183013>",
                 "Joker": "<:joker:1277311435235655746>",
                 "Hero": "<:hero:1277310763442372672>",
                 "Banjo-Kazooie": "<:banjokazooie:1277310491626049649>",
                 "Terry": "<:terry:1277312566993092795>",
                 "Byleth": "<:byleth:1277310550484844715>",
                 "Min Min": "<:minmin:1277311955992051777>",
                 "Steve": "<:steve:1277312551767642205>",
                 "Sephiroth": "<:sephiroth:1277312401666211933>",
                 "Pyra Mythra": "<:pyramythra:1277312221877375047>",
                 "Kazuya": "<:kazuya:1277311610779603034>",
                 "Sora": "<:sora:1277312535330291813>",
                 "Random": "<:random:1277312239254376511>"}
# And another one for other emojis XD
botEmojis = {"DownArrow": "<:RedArrowDown:1277676225980268594>",
             "UpArrow": "<:GreenArrowUp:1277676202315874476>",
             "YellowDash": "<:DashYellow:1277676186364805121>"}

# Setup but
intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='sb!', intents=intents)

# Send message when logged in
@bot.event
async def on_ready():
    # Print when logged in
    print("=" * 50)
    print(f'✅ Logged in as {bot.user.name}')
    print("=" * 50)
    # Send embed in "Zona Flori" (Los Panitas)
    channel = bot.get_channel(1277272930451198067)
    embed = nextcord.Embed(
        title="<:GreenSmashBall:1277306606484193280>  Bot Encendido",
        description=f"Logged in as *{bot.user.name}*",
        color=nextcord.Color.green()
    )

    await channel.send(embed=embed)

# Refresh database (Quite heavy code)
@bot.slash_command(name="actualizar", description="Actualiza toda la información de los perfiles", guild_ids=[testServerId])
async def refresh(interaction:Interaction):
    # Embed warning (this process takes quite a while)
    embed = nextcord.Embed(
        title="❗ El bot se está actualizando",
        description="Este proceso tardará unos minutos, mientras tanto el bot no va a responder",
        color = 0xD3D3D3
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1277272930451198067/1277365949258797147/GreenSmashBall.png?ex=66cce73e&is=66cb95be&hm=aefa281e1eca2a14cb72403ed35ee30d40ee29af6d4099ebfcb4895dceaa80d7&")
    await interaction.send(embed=embed)
    # Start updating
    getArgRankProfiles()

# Show SSBU official tierlist (Just sends an image)
@bot.slash_command(name="tierlist", description= "Envía una imagen de la Tierlist oficial", guild_ids=[testServerId])
async def tierList(interaction: Interaction):
    await interaction.send("https://cdn.discordapp.com/attachments/1277272930451198067/1278080491815436391/Imagen_de_WhatsApp_2024-08-27_a_las_16.43.37_0922c79a.jpg?ex=66cf80b6&is=66ce2f36&hm=c210a51e8667479107a32d00ffe20cb87b49bb1bdb391464ff806dfa5db11852&")

# Search player by name
@bot.slash_command(name="perfil", description="Busca el perfil de un jugador por nombre", guild_ids=[testServerId])
async def searchProfileByName(interaction: Interaction, nombre: str):
    # Get user object
    playerProfile = Players.searchPlayer(nombre)
    # Code if player is not found

    # Construct error embed
    errorEmbed = nextcord.Embed(
        title="<:random:1277312239254376511> Jugador no encontrado",
        description=f"No se encontró el perfil de **{nombre}**",
        color=0xFF0000
    )
    errorEmbed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1277272930451198067/1277350852482437243/RedSmashBall.png?ex=66ccd92f&is=66cb87af&hm=7f2c4565c2e64bc7ab5f10663f18410349f0bd60c3ae0d73f226e9f22523f346&")
    # Check if player is not found
    if playerProfile == "NOTFOUND":
        await interaction.send(embed=errorEmbed)
        return
    
    # If player is found

    top3 = False
    # Set color depending on top
    if playerProfile.pos == 1:
        # Gold for top 1 and stupid image
        sideColor = 0xFFD700
        top3 = True
        topImg = "https://www.shutterstock.com/shutterstock/photos/402019894/display_1500/stock-photo-the-d-guy-and-the-top-402019894.jpg"
    elif playerProfile.pos == 2:
        # Silver for top 2
        sideColor = 0xC0C0C0
        top3 = True
        topImg = "https://www.shutterstock.com/shutterstock/photos/402019867/display_1500/stock-photo-the-d-guy-and-the-top-402019867.jpg"
    elif playerProfile.pos == 3:
        # Bronze for top 3
        sideColor = 0xCD7F32
        top3 = True
        topImg = "https://www.shutterstock.com/shutterstock/photos/402019843/display_1500/stock-photo-the-d-guy-and-the-top-402019843.jpg"
    elif playerProfile.pos < 11:
        # Purple for top 10
        sideColor = 0x800080
    elif playerProfile.pos < 31:
        # Blue for top 30
        sideColor = 0x0000FF
    elif playerProfile.pos < 51:
        # Green for top 50
        sideColor = 0x00FF00
    elif playerProfile.pos > 50:
        # White for above 50
        sideColor = 0xFFFFFF
    # Set main
    if len(playerProfile.mains) < 1:
        # For image
        main = "Random"
        # For listing
        mains = "<:random:1277312239254376511>"
    else:
        main = playerProfile.mains[0]
        mains = ""
        for pj in playerProfile.mains:
            mains += str(ssbuRosterEmojis[pj]) + str(pj) + "\n"
    # Link to profile
    url = "https://braacket.com/league/ArgRank2024/player/" + str(playerProfile.code)
    # String maker for Tournament History (Max 8 tourneis)
    thStr = ""
    #n = 0
    for i in range(len(playerProfile.tournNames)):
        #n += 1
        thStr += ":trophy: **" + playerProfile.tournNames[i] + "** - " + playerProfile.tournRank[i] + " / " + playerProfile.tournMaxRank[i] + "\n"
    # Get emoji for Winrate
    winRate = int(playerProfile.winrate[:len(playerProfile.winrate) - 1])
    if winRate < 50:
        wrEmoji = botEmojis["DownArrow"]
    elif winRate < 61:
        wrEmoji = botEmojis["YellowDash"]
    else:
        wrEmoji = botEmojis["UpArrow"]

    # Embed for profile
    embed = nextcord.Embed(
        title=playerProfile.name,
        description="TOP **" + str(playerProfile.pos) + "** Argentina\n**" + str(wrEmoji) + " " + playerProfile.winrate + "** Winrate\n" + "[Perfil Completo](<" + url + ">)",
        color=sideColor
    )
    # Field for Mains
    embed.add_field(name="Mains", value=mains, inline=False)
    # Field for Tournament History
    embed.add_field(name="Historial de Torneos (Últimos 12)", value=thStr)
    # Author
    embed.set_author(name=bot.user.name,
                     icon_url="https://ssb.wiki.gallery/images/thumb/a/a2/SSBU_spirit_Smash_Ball.png/250px-SSBU_spirit_Smash_Ball.png")
    if top3: 
        embed.set_image(url=topImg) 
    # Thumbnail
    embed.set_thumbnail(url=ssbuRosterProfileImg[main])

    # I dont know what the fuck happens here but sometimes it just triggers a Traceback
    try:
        await interaction.send(embed=embed)
        print("✅ Showing profile:", nombre)
    except:
        print("❌ Error ocurred")

# Search player by top
@bot.slash_command(name="top", description="Muestra el perfil del top que quieras", guild_ids=[testServerId])
async def searchProfileByTop(interaction: Interaction, top: int):
    # Get user object
    playerProfile = Players.searchPlayer(top)
    # Code if player is not found

    # Construct error embed
    errorEmbed = nextcord.Embed(
        title="<:random:1277312239254376511> Jugador no encontrado",
        description=f"Top **{top}** fuera de rango (1 - {rows})",
        color=0xFF0000
    )
    errorEmbed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1277272930451198067/1277350852482437243/RedSmashBall.png?ex=66ccd92f&is=66cb87af&hm=7f2c4565c2e64bc7ab5f10663f18410349f0bd60c3ae0d73f226e9f22523f346&")
    # Check if player is not found
    if playerProfile == "NOTFOUND":
        await interaction.send(embed=errorEmbed)
        return
    
    # If player is found

    top3 = False
    # Set color depending on top
    if playerProfile.pos == 1:
        # Gold for top 1 and stupid image
        sideColor = 0xFFD700
        top3 = True
        topImg = "https://www.shutterstock.com/shutterstock/photos/402019894/display_1500/stock-photo-the-d-guy-and-the-top-402019894.jpg"
    elif playerProfile.pos == 2:
        # Silver for top 2
        sideColor = 0xC0C0C0
        top3 = True
        topImg = "https://www.shutterstock.com/shutterstock/photos/402019867/display_1500/stock-photo-the-d-guy-and-the-top-402019867.jpg"
    elif playerProfile.pos == 3:
        # Bronze for top 3
        sideColor = 0xCD7F32
        top3 = True
        topImg = "https://www.shutterstock.com/shutterstock/photos/402019843/display_1500/stock-photo-the-d-guy-and-the-top-402019843.jpg"
    elif playerProfile.pos < 11:
        # Purple for top 10
        sideColor = 0x800080
    elif playerProfile.pos < 31:
        # Blue for top 30
        sideColor = 0x0000FF
    elif playerProfile.pos < 51:
        # Green for top 50
        sideColor = 0x00FF00
    elif playerProfile.pos > 50:
        # White for above 50
        sideColor = 0xFFFFFF
    # Set main
    if len(playerProfile.mains) < 1:
        # For image
        main = "Random"
        # For listing
        mains = "<:random:1277312239254376511>"
    else:
        main = playerProfile.mains[0]
        mains = ""
        for pj in playerProfile.mains:
            mains += str(ssbuRosterEmojis[pj]) + str(pj) + "\n"
    # Link to profile
    url = "https://braacket.com/league/ArgRank2024/player/" + str(playerProfile.code)
    # String maker for Tournament History (Max 8 tourneis)
    thStr = ""
    #n = 0
    for i in range(len(playerProfile.tournNames)):
        #n += 1
        thStr += ":trophy: **" + playerProfile.tournNames[i] + "** - " + playerProfile.tournRank[i] + " / " + playerProfile.tournMaxRank[i] + "\n"
    # Get emoji for Winrate
    winRate = int(playerProfile.winrate[:len(playerProfile.winrate) - 1])
    if winRate < 50:
        wrEmoji = botEmojis["DownArrow"]
    elif winRate < 61:
        wrEmoji = botEmojis["YellowDash"]
    else:
        wrEmoji = botEmojis["UpArrow"]

    # Embed for profile
    embed = nextcord.Embed(
        title=playerProfile.name,
        description="TOP **" + str(playerProfile.pos) + "** Argentina\n**" + str(wrEmoji) + " " + playerProfile.winrate + "** Winrate\n" + "[Perfil Completo](<" + url + ">)",
        color=sideColor
    )
    # Field for Mains
    embed.add_field(name="Mains", value=mains, inline=False)
    # Field for Tournament History
    embed.add_field(name="Historial de Torneos (Últimos 12)", value=thStr)
    # Author
    embed.set_author(name=bot.user.name,
                     icon_url="https://ssb.wiki.gallery/images/thumb/a/a2/SSBU_spirit_Smash_Ball.png/250px-SSBU_spirit_Smash_Ball.png")
    if top3: 
        embed.set_image(url=topImg) 
    # Thumbnail
    embed.set_thumbnail(url=ssbuRosterProfileImg[main])

    # I dont know what the fuck happens here but sometimes it just triggers a Traceback
    try:
        await interaction.send(embed=embed)
        print("✅ Showing top:", top)
    except:
        print("❌ Error ocurred")

""" ===================================================================== """

# Run bot with token
bot.run('MTIzMzU4MTU0MzE4OTEyMzA4Mw.GiMfC8.fTOxx_5vRtYIW7sA7GdgA8z--lPeUC3txMVr3U')