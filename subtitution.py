text = list("""izu gjweft yifgx izji tjluy wf yuwyu yijgiy frr vkiz jw kdu dgujt igadl j dzur jwe j hkudu fr hpaif.
izu maxy izji fvwue izu kdu dgujt igadl yifpu izu hkudu fr hpaif rgft izu hjyigx dzur vzf fnijkwue ki rgft izu rpxkwm upuhzjwi.
izu rpxkwm upuhzjwi mfi ki rgft j yatf vguyipug vzf fnijkwue ki kw izu yatf dzjthkfwyzkh fw yjiagw.
izux vuwi if yjiagw nudjayu qahkiug vjy rapp fr taijwi nujsdffwy.
izu nujsdffwy vugu rgft tjgy vzugu izu nannpx nannpuy, jw jwdkuwi rjwm izji vjy nagkue kw djtupfi pksue.
izu nannpx nannpuy djtu njdl jiug izu dpfvwy guyaggudiue zkt kw jw jwdkuwi nagkjp yhupp fr tjmkdjpwuyy.
izuw izu dfgwefm rgft suway puje jw jiijdl fr djwfuy fwif izu gayykjwy vzf guyhfweue nx ijlkwm tdefwjpey jvjx rgft dzkwj.
ykwdu dzkwj ekew'i zjsu jwxtfgu tdefwjpey izux eudkeue if nax j hkccj zai.
izu hkccj zai vjy izuw yifpuw nx j ijplkwm upuhzjwi rgft kwekj.
izu upuhzjwi vjy izu maga'y jwe zu pksue ji izu jyzgjt kw pfy jwmupuy.
izu upuhzjwi zje j hkm rgkuwe vzf ijamzi tjiz.
izu hkm ubhpfeue fwu ejx jwe puri izu vzfpu vfgpe vfweugkwm.
ykwdu izu hkm ubhpfeue izu lkwm hkm npjtue izu mkjwiy.
ykwdu izu mkjwiy zjiue nukwm npjtue izux pue jw jiijdl fw izu lkwm jwe ykwdu izux vugu fr dfagyu tadz nkmmug izux vugu skdifgkfay.
jriug izu mkjwiy iffl dfwigfp fr mguuwpjwe izux yijgiue rkmzikwm izu sklkwmy rgft kdupjwe.
izu fhhfwuwiy vugu uouwpx tjidzue yf izux uweue ah euyigfxkwm ujdz fizug jwe izux nudjtu ubikwdi.
izuw izu mfgkppjy yifpu izu zfwej igjkp 70'y rgft ifwx yfhgjwf izu puje mjwmyiug rgft kijpx.
ifwx yfhgjwf jdiajppx mfi izu zfwej'y rgft kwekj jwxzfv njdl if izu mfgkppjy.
izu mfgkppjy yijgiue djaykwm j galay kw izu nkm jhhpu, jdiajppx j nkm jhhpu, vzugu izux gjw fsug nkppx qfu jwe ukpuuw.
ykwdu izu rffinjpp hpjxugy vugu dzjykwm izut izu mfgkppjy zfhhue kwif izu mkjwi hujdz vkiz qjtuy vzf vjy uydjhkwm zky uskp hjguwiy.
izu yifgx uwey izugu k't yfggx if yjx nai fz vupp zux, zux, zux.
izu rpjm ky "izux jpp pksue zjhhkpx uoug jriug".""")

Dic = {
        "a":"u",
        "b":"x",
        "c":"z",
        "d":"c",
        "e":"d",
        "f":"o",
        "g":"r",
        "h":"p",
        "i":"t",
        "j":"a",
        "k":"i",
        "l":"k",
        "m":"g",
        "n":"b",
        "o":"v",
        "p":"l",
        "q":"j",
        "r":"f",
        "s":"v",
        "t":"m",
        "u":"e",
        "v":"w",
        "w":"n",
        "x":"y",
        "y":"s",
        "z":"h",
    }

for char, rep in Dic.items():
    for indx, lett in enumerate(text):
        if char == lett:
            text[indx] = "++" + rep
text = ''.join(text)
text = text.replace("++", "")
print(text)
