---
entity_id: "protein.P0A9Q1"
entity_type: "protein"
name: "arcA"
source_database: "UniProt"
source_id: "P0A9Q1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "arcA cpxC dye fexA msp seg sfrA b4401 JW4364"
---

# arcA

`protein.P0A9Q1`

## Static

- Type: `protein`
- Source: `UniProt:P0A9Q1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system ArcB/ArcA. Represses a wide variety of aerobic enzymes under anaerobic conditions. Controls the resistance of E.coli to dyes; required for expression of the alkaline phosphatase and sex factor F genes; it may also be involved in the osmoregulation of envelope proteins. When activated by ArcB, it negatively regulates the expression of genes of aerobic function. Activates the transcription of the plfB operon by binding to its promoter. ArcA is a dual transcriptional regulator for Anoxic redox control . It acts primarily as a negative transcriptional regulator under anaerobic conditions. ArcA represses operons involved in respiratory metabolism, including those that encode products such as the tricarboxylic acid cycle enzymes, enzymes of the glyoxylate shunt, and enzymes of the pathway for fatty acid degradation . In addition, ArcA acts as a repressor for rpoS transcription . ArcA also activates a few operons encoding proteins involved in fermentative metabolism . It has been identified as global repressor of carbon oxidation pathways . Microarray analyses have identified a large number of genes affected by ArcA and have revealed that the Arc system and the FNR regulatory network overlap to a much greater extent than previously estimated...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system ArcB/ArcA. Represses a wide variety of aerobic enzymes under anaerobic conditions. Controls the resistance of E.coli to dyes; required for expression of the alkaline phosphatase and sex factor F genes; it may also be involved in the osmoregulation of envelope proteins. When activated by ArcB, it negatively regulates the expression of genes of aerobic function. Activates the transcription of the plfB operon by binding to its promoter.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (150)

- `activates` --> [[gene.b0032|gene.b0032]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=carA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b0699|gene.b0699]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=ybfA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b0721|gene.b0721]] `RegulonDB` `S` - regulator=ArcA; target=sdhC; function=-+
- `activates` --> [[gene.b0722|gene.b0722]] `RegulonDB` `S` - regulator=ArcA; target=sdhD; function=-+
- `activates` --> [[gene.b0723|gene.b0723]] `RegulonDB` `S` - regulator=ArcA; target=sdhA; function=-+
- `activates` --> [[gene.b0724|gene.b0724]] `RegulonDB` `S` - regulator=ArcA; target=sdhB; function=-+
- `activates` --> [[gene.b0726|gene.b0726]] `RegulonDB` `S` - regulator=ArcA; target=sucA; function=-+
- `activates` --> [[gene.b0727|gene.b0727]] `RegulonDB` `S` - regulator=ArcA; target=sucB; function=-+
- `activates` --> [[gene.b0728|gene.b0728]] `RegulonDB` `S` - regulator=ArcA; target=sucC; function=-+
- `activates` --> [[gene.b0729|gene.b0729]] `RegulonDB` `S` - regulator=ArcA; target=sucD; function=-+
- `activates` --> [[gene.b0733|gene.b0733]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=cydA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b0826|gene.b0826]] `RegulonDB` `S` - regulator=ArcA; target=moeB; function=+
- `activates` --> [[gene.b0827|gene.b0827]] `RegulonDB` `S` - regulator=ArcA; target=moeA; function=+
- `activates` --> [[gene.b0886|gene.b0886]] `RegulonDB` `S` - regulator=ArcA; target=cydC; function=+
- `activates` --> [[gene.b0887|gene.b0887]] `RegulonDB` `S` - regulator=ArcA; target=cydD; function=+
- `activates` --> [[gene.b0904|gene.b0904]] `RegulonDB` `C` - regulator=ArcA; target=focA; function=-+
- `activates` --> [[gene.b0931|gene.b0931]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=pncB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b0974|gene.b0974]] `RegulonDB` `S` - regulator=ArcA; target=hyaC; function=+
- `activates` --> [[gene.b1006|gene.b1006]] `RegulonDB` `S` - regulator=ArcA; target=rutG; function=+
- `activates` --> [[gene.b1007|gene.b1007]] `RegulonDB` `S` - regulator=ArcA; target=rutF; function=+
- `activates` --> [[gene.b1008|gene.b1008]] `RegulonDB` `S` - regulator=ArcA; target=rutE; function=+
- `activates` --> [[gene.b1009|gene.b1009]] `RegulonDB` `S` - regulator=ArcA; target=rutD; function=+
- `activates` --> [[gene.b1010|gene.b1010]] `RegulonDB` `S` - regulator=ArcA; target=rutC; function=+
- `activates` --> [[gene.b1011|gene.b1011]] `RegulonDB` `S` - regulator=ArcA; target=rutB; function=+
- `activates` --> [[gene.b1012|gene.b1012]] `RegulonDB` `S` - regulator=ArcA; target=rutA; function=+
- `activates` --> [[gene.b1094|gene.b1094]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=acpP; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1185|gene.b1185]] `RegulonDB` `S` - regulator=ArcA; target=dsbB; function=+
- `activates` --> [[gene.b1243|gene.b1243]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=oppA; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1603|gene.b1603]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=pntA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1608|gene.b1608]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=rstA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1613|gene.b1613]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=manA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2380|gene.b2380]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=pyrS; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2393|gene.b2393]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=nupC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2581|gene.b2581]] `RegulonDB` `S` - regulator=ArcA; target=yfiF; function=+
- `activates` --> [[gene.b3089|gene.b3089]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=sstT; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3237|gene.b3237]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=argR; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3398|gene.b3398]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=igaA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3402|gene.b3402]] `RegulonDB` `S` - regulator=ArcA; target=yhgE; function=+
- `activates` --> [[gene.b3512|gene.b3512]] `RegulonDB` `S` - regulator=ArcA; target=gadE; function=+
- `activates` --> [[gene.b3544|gene.b3544]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=dppA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3783|gene.b3783]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=rho; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3821|gene.b3821]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=pldA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4123|gene.b4123]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=dcuB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4138|gene.b4138]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=dcuA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4401|gene.b4401]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=arcA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4439|gene.b4439]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=micF; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4443|gene.b4443]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=gcvB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4718|gene.b4718]] `RegulonDB` `S` - regulator=ArcA; target=gadF; function=+
- `activates` --> [[gene.b4764|gene.b4764]] `RegulonDB` `S` - regulator=ArcA; target=sdhX; function=-+
- `represses` --> [[gene.b0002|gene.b0002]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=thrA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0116|gene.b0116]] `RegulonDB` `S` - regulator=ArcA; target=lpd; function=-
- `represses` --> [[gene.b0118|gene.b0118]] `RegulonDB` `S` - regulator=ArcA; target=acnB; function=-
- `represses` --> [[gene.b0221|gene.b0221]] `RegulonDB|EcoCyc` `C` - regulator=ArcA; target=fadE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0311|gene.b0311]] `RegulonDB` `S` - regulator=ArcA; target=betA; function=-
- `represses` --> [[gene.b0314|gene.b0314]] `RegulonDB` `S` - regulator=ArcA; target=betT; function=-
- `represses` --> [[gene.b0428|gene.b0428]] `RegulonDB` `C` - regulator=ArcA; target=cyoE; function=-
- `represses` --> [[gene.b0429|gene.b0429]] `RegulonDB` `C` - regulator=ArcA; target=cyoD; function=-
- `represses` --> [[gene.b0430|gene.b0430]] `RegulonDB` `C` - regulator=ArcA; target=cyoC; function=-
- `represses` --> [[gene.b0431|gene.b0431]] `RegulonDB` `C` - regulator=ArcA; target=cyoB; function=-
- `represses` --> [[gene.b0432|gene.b0432]] `RegulonDB|EcoCyc` `C` - regulator=ArcA; target=cyoA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0698|gene.b0698]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=kdpA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0720|gene.b0720]] `RegulonDB` `C` - regulator=ArcA; target=gltA; function=-
- `represses` --> [[gene.b0721|gene.b0721]] `RegulonDB` `S` - regulator=ArcA; target=sdhC; function=-+
- `represses` --> [[gene.b0722|gene.b0722]] `RegulonDB` `S` - regulator=ArcA; target=sdhD; function=-+
- `represses` --> [[gene.b0723|gene.b0723]] `RegulonDB` `S` - regulator=ArcA; target=sdhA; function=-+
- `represses` --> [[gene.b0724|gene.b0724]] `RegulonDB` `S` - regulator=ArcA; target=sdhB; function=-+
- `represses` --> [[gene.b0726|gene.b0726]] `RegulonDB` `S` - regulator=ArcA; target=sucA; function=-+
- `represses` --> [[gene.b0727|gene.b0727]] `RegulonDB` `S` - regulator=ArcA; target=sucB; function=-+
- `represses` --> [[gene.b0728|gene.b0728]] `RegulonDB` `S` - regulator=ArcA; target=sucC; function=-+
- `represses` --> [[gene.b0729|gene.b0729]] `RegulonDB` `S` - regulator=ArcA; target=sucD; function=-+
- `represses` --> [[gene.b0821|gene.b0821]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=ybiU; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0854|gene.b0854]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=potF; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0904|gene.b0904]] `RegulonDB|EcoCyc` `C` - regulator=ArcA; target=focA; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0932|gene.b0932]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=pepN; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0953|gene.b0953]] `RegulonDB` `S` - regulator=ArcA; target=rmf; function=-
- `represses` --> [[gene.b1014|gene.b1014]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=putA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1015|gene.b1015]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=putP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1020|gene.b1020]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=phoH; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1101|gene.b1101]] `RegulonDB` `S` - regulator=ArcA; target=ptsG; function=-
- `represses` --> [[gene.b1109|gene.b1109]] `RegulonDB` `S` - regulator=ArcA; target=ndh; function=-
- `represses` --> [[gene.b1136|gene.b1136]] `RegulonDB` `C` - regulator=ArcA; target=icd; function=-
- `represses` --> [[gene.b1243|gene.b1243]] `RegulonDB` `S` - regulator=ArcA; target=oppA; function=-+
- `represses` --> [[gene.b1256|gene.b1256]] `RegulonDB` `S` - regulator=ArcA; target=ompW; function=-
- `represses` --> [[gene.b1297|gene.b1297]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=puuA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1298|gene.b1298]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=puuD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1324|gene.b1324]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=tpx; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1332|gene.b1332]] `RegulonDB` `S` - regulator=ArcA; target=ynaJ; function=-
- `represses` --> [[gene.b1415|gene.b1415]] `RegulonDB|EcoCyc` `C` - regulator=ArcA; target=aldA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1451|gene.b1451]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=pqqU; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1452|gene.b1452]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=yncE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1607|gene.b1607]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=ydgC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1612|gene.b1612]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=fumA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1749|gene.b1749]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=xthA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1778|gene.b1778]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=msrB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1805|gene.b1805]] `RegulonDB` `C` - regulator=ArcA; target=fadD; function=-
- `represses` --> [[gene.b2153|gene.b2153]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=folE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2172|gene.b2172]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=yeiQ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2181|gene.b2181]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=yejG; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2210|gene.b2210]] `RegulonDB` `S` - regulator=ArcA; target=mqo; function=-
- `represses` --> [[gene.b2276|gene.b2276]] `RegulonDB` `C` - regulator=ArcA; target=nuoN; function=-
- `represses` --> [[gene.b2277|gene.b2277]] `RegulonDB` `C` - regulator=ArcA; target=nuoM; function=-
- `represses` --> [[gene.b2278|gene.b2278]] `RegulonDB` `C` - regulator=ArcA; target=nuoL; function=-
- `represses` --> [[gene.b2279|gene.b2279]] `RegulonDB` `C` - regulator=ArcA; target=nuoK; function=-
- `represses` --> [[gene.b2280|gene.b2280]] `RegulonDB` `C` - regulator=ArcA; target=nuoJ; function=-
- `represses` --> [[gene.b2281|gene.b2281]] `RegulonDB` `C` - regulator=ArcA; target=nuoI; function=-
- `represses` --> [[gene.b2282|gene.b2282]] `RegulonDB` `C` - regulator=ArcA; target=nuoH; function=-
- `represses` --> [[gene.b2283|gene.b2283]] `RegulonDB` `C` - regulator=ArcA; target=nuoG; function=-
- `represses` --> [[gene.b2284|gene.b2284]] `RegulonDB` `C` - regulator=ArcA; target=nuoF; function=-
- `represses` --> [[gene.b2285|gene.b2285]] `RegulonDB` `C` - regulator=ArcA; target=nuoE; function=-
- `represses` --> [[gene.b2286|gene.b2286]] `RegulonDB` `C` - regulator=ArcA; target=nuoC; function=-
- `represses` --> [[gene.b2287|gene.b2287]] `RegulonDB` `C` - regulator=ArcA; target=nuoB; function=-
- `represses` --> [[gene.b2288|gene.b2288]] `RegulonDB` `C` - regulator=ArcA; target=nuoA; function=-
- `represses` --> [[gene.b2310|gene.b2310]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=argT; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2341|gene.b2341]] `RegulonDB` `S` - regulator=ArcA; target=fadJ; function=-
- `represses` --> [[gene.b2342|gene.b2342]] `RegulonDB` `S` - regulator=ArcA; target=fadI; function=-
- `represses` --> [[gene.b2344|gene.b2344]] `RegulonDB` `S` - regulator=ArcA; target=fadL; function=-
- `represses` --> [[gene.b2518|gene.b2518]] `RegulonDB` `S` - regulator=ArcA; target=ndk; function=-
- `represses` --> [[gene.b2587|gene.b2587]] `RegulonDB` `S` - regulator=ArcA; target=kgtP; function=-
- `represses` --> [[gene.b2659|gene.b2659]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=glaH; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2741|gene.b2741]] `RegulonDB` `S` - regulator=ArcA; target=rpoS; function=-
- `represses` --> [[gene.b2975|gene.b2975]] `RegulonDB` `C` - regulator=ArcA; target=glcA; function=-
- `represses` --> [[gene.b2976|gene.b2976]] `RegulonDB` `C` - regulator=ArcA; target=glcB; function=-
- `represses` --> [[gene.b2977|gene.b2977]] `RegulonDB` `C` - regulator=ArcA; target=glcG; function=-
- `represses` --> [[gene.b2979|gene.b2979]] `RegulonDB` `C` - regulator=ArcA; target=glcD; function=-
- `represses` --> [[gene.b2980|gene.b2980]] `RegulonDB|EcoCyc` `C` - regulator=ArcA; target=glcC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3081|gene.b3081]] `RegulonDB` `S` - regulator=ArcA; target=fadH; function=-
- `represses` --> [[gene.b3236|gene.b3236]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3397|gene.b3397]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=nudE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3408|gene.b3408]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=feoA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3425|gene.b3425]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=glpE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3426|gene.b3426]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=glpD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3523|gene.b3523]] `RegulonDB` `S` - regulator=ArcA; target=yhjE; function=-
- `represses` --> [[gene.b3603|gene.b3603]] `RegulonDB` `C` - regulator=ArcA; target=lldP; function=-
- `represses` --> [[gene.b3604|gene.b3604]] `RegulonDB` `C` - regulator=ArcA; target=lldR; function=-
- `represses` --> [[gene.b3605|gene.b3605]] `RegulonDB` `C` - regulator=ArcA; target=lldD; function=-
- `represses` --> [[gene.b3712|gene.b3712]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=yieE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3820|gene.b3820]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=yigI; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3845|gene.b3845]] `RegulonDB` `C` - regulator=ArcA; target=fadA; function=-
- `represses` --> [[gene.b3846|gene.b3846]] `RegulonDB` `C` - regulator=ArcA; target=fadB; function=-
- `represses` --> [[gene.b3962|gene.b3962]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=sthA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3994|gene.b3994]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=thiC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3995|gene.b3995]] `RegulonDB` `S` - regulator=ArcA; target=rsd; function=-
- `represses` --> [[gene.b4058|gene.b4058]] `RegulonDB` `S` - regulator=ArcA; target=uvrA; function=-
- `represses` --> [[gene.b4059|gene.b4059]] `RegulonDB` `S` - regulator=ArcA; target=ssb; function=-
- `represses` --> [[gene.b4208|gene.b4208]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=cycA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b4340|gene.b4340]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=yjiR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b4376|gene.b4376]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=osmY; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b4467|gene.b4467]] `RegulonDB` `C` - regulator=ArcA; target=glcF; function=-
- `represses` --> [[gene.b4468|gene.b4468]] `RegulonDB` `C` - regulator=ArcA; target=glcE; function=-
- `represses` --> [[gene.b4764|gene.b4764]] `RegulonDB` `S` - regulator=ArcA; target=sdhX; function=-+

## Incoming Edges (1)

- `encodes` <-- [[gene.b4401|gene.b4401]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9Q1`
- `KEGG:ecj:JW4364;eco:b4401;ecoc:C3026_23780;`
- `GeneID:86862515;93777444;948874;`
- `GO:GO:0000156; GO:0000160; GO:0000976; GO:0001217; GO:0003700; GO:0005829; GO:0006355; GO:0032993; GO:0042802; GO:0045892; GO:0045893`

## Notes

Aerobic respiration control protein ArcA (Dye resistance protein)
