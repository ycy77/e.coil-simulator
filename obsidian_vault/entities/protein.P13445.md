---
entity_id: "protein.P13445"
entity_type: "protein"
name: "rpoS"
source_database: "UniProt"
source_id: "P13445"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00959}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpoS appR katF nur otsX sigS b2741 JW5437"
---

# rpoS

`protein.P13445`

## Static

- Type: `protein`
- Source: `UniProt:P13445`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00959}.

## Enriched Summary

FUNCTION: Sigma factors are initiation factors that promote the attachment of RNA polymerase to specific initiation sites and are then released. This sigma factor is the master transcriptional regulator of the stationary phase and the general stress response. Controls, positively or negatively, the expression of several hundred genes, which are mainly involved in metabolism, transport, regulation and stress management. {ECO:0000255|HAMAP-Rule:MF_00959, ECO:0000269|PubMed:15558318, ECO:0000269|PubMed:15716429, ECO:0000269|PubMed:16511888, ECO:0000269|PubMed:21398637, ECO:0000269|PubMed:8475100}.; FUNCTION: Protects stationary phase cells from killing induced by endoribonuclease MazF. {ECO:0000269|PubMed:19251848}. rpoS encodes the alternative sigma factor σS, a subunit of RNA polymerase that acts as the master regulator of the general stress response in E. coli. Genome-wide analyses of RpoS-dependent gene expression showed that up to 10% of the genes in E. coli are under direct or indirect control of σS . RNA polymerase bound to σS efficiently transcribes genes involved in stress responses and secondary metabolism, as well as RNAs from intergenic regions with yet-unknown function(s). The effects of σS on E. coli metabolism have been investigated...

## Biological Role

Component of RNA polymerase sigma S (complex.ecocyc.RNAPS-CPLX).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Sigma factors are initiation factors that promote the attachment of RNA polymerase to specific initiation sites and are then released. This sigma factor is the master transcriptional regulator of the stationary phase and the general stress response. Controls, positively or negatively, the expression of several hundred genes, which are mainly involved in metabolism, transport, regulation and stress management. {ECO:0000255|HAMAP-Rule:MF_00959, ECO:0000269|PubMed:15558318, ECO:0000269|PubMed:15716429, ECO:0000269|PubMed:16511888, ECO:0000269|PubMed:21398637, ECO:0000269|PubMed:8475100}.; FUNCTION: Protects stationary phase cells from killing induced by endoribonuclease MazF. {ECO:0000269|PubMed:19251848}.

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (215)

- `activates` --> [[gene.b0065|gene.b0065]] `RegulonDB` `S` - sigma=sigma38; target=yabI; function=+
- `activates` --> [[gene.b0070|gene.b0070]] `RegulonDB` `S` - sigma=sigma38; target=setA; function=+
- `activates` --> [[gene.b0093|gene.b0093]] `RegulonDB` `S` - sigma=sigma38; target=ftsQ; function=+
- `activates` --> [[gene.b0094|gene.b0094]] `RegulonDB` `S` - sigma=sigma38; target=ftsA; function=+
- `activates` --> [[gene.b0095|gene.b0095]] `RegulonDB` `S` - sigma=sigma38; target=ftsZ; function=+
- `activates` --> [[gene.b0113|gene.b0113]] `RegulonDB` `C` - sigma=sigma38; target=pdhR; function=+
- `activates` --> [[gene.b0114|gene.b0114]] `RegulonDB` `C` - sigma=sigma38; target=aceE; function=+
- `activates` --> [[gene.b0115|gene.b0115]] `RegulonDB` `C` - sigma=sigma38; target=aceF; function=+
- `activates` --> [[gene.b0116|gene.b0116]] `RegulonDB` `C` - sigma=sigma38; target=lpd; function=+
- `activates` --> [[gene.b0139|gene.b0139]] `RegulonDB` `S` - sigma=sigma38; target=htrE; function=+
- `activates` --> [[gene.b0140|gene.b0140]] `RegulonDB` `S` - sigma=sigma38; target=yadV; function=+
- `activates` --> [[gene.b0142|gene.b0142]] `RegulonDB` `S` - sigma=sigma38; target=folK; function=+
- `activates` --> [[gene.b0143|gene.b0143]] `RegulonDB` `S` - sigma=sigma38; target=pcnB; function=+
- `activates` --> [[gene.b0157|gene.b0157]] `RegulonDB` `S` - sigma=sigma38; target=yadS; function=+
- `activates` --> [[gene.b0158|gene.b0158]] `RegulonDB` `S` - sigma=sigma38; target=btuF; function=+
- `activates` --> [[gene.b0159|gene.b0159]] `RegulonDB` `S` - sigma=sigma38; target=mtn; function=+
- `activates` --> [[gene.b0385|gene.b0385]] `RegulonDB` `S` - sigma=sigma38; target=dgcC; function=+
- `activates` --> [[gene.b0435|gene.b0435]] `RegulonDB` `C` - sigma=sigma38; target=bolA; function=+
- `activates` --> [[gene.b0485|gene.b0485]] `RegulonDB` `S` - sigma=sigma38; target=glsA; function=+
- `activates` --> [[gene.b0486|gene.b0486]] `RegulonDB` `S` - sigma=sigma38; target=ybaT; function=+
- `activates` --> [[gene.b0707|gene.b0707]] `RegulonDB` `S` - sigma=sigma38; target=ybgA; function=+
- `activates` --> [[gene.b0708|gene.b0708]] `RegulonDB` `S` - sigma=sigma38; target=phr; function=+
- `activates` --> [[gene.b0726|gene.b0726]] `RegulonDB` `S` - sigma=sigma38; target=sucA; function=+
- `activates` --> [[gene.b0727|gene.b0727]] `RegulonDB` `S` - sigma=sigma38; target=sucB; function=+
- `activates` --> [[gene.b0728|gene.b0728]] `RegulonDB` `S` - sigma=sigma38; target=sucC; function=+
- `activates` --> [[gene.b0729|gene.b0729]] `RegulonDB` `S` - sigma=sigma38; target=sucD; function=+
- `activates` --> [[gene.b0755|gene.b0755]] `RegulonDB` `S` - sigma=sigma38; target=gpmA; function=+
- `activates` --> [[gene.b0756|gene.b0756]] `RegulonDB` `C` - sigma=sigma38; target=galM; function=+
- `activates` --> [[gene.b0757|gene.b0757]] `RegulonDB` `C` - sigma=sigma38; target=galK; function=+
- `activates` --> [[gene.b0758|gene.b0758]] `RegulonDB` `C` - sigma=sigma38; target=galT; function=+
- `activates` --> [[gene.b0759|gene.b0759]] `RegulonDB` `C` - sigma=sigma38; target=galE; function=+
- `activates` --> [[gene.b0812|gene.b0812]] `RegulonDB` `S` - sigma=sigma38; target=dps; function=+
- `activates` --> [[gene.b0861|gene.b0861]] `RegulonDB` `S` - sigma=sigma38; target=artM; function=+
- `activates` --> [[gene.b0862|gene.b0862]] `RegulonDB` `S` - sigma=sigma38; target=artQ; function=+
- `activates` --> [[gene.b0863|gene.b0863]] `RegulonDB` `S` - sigma=sigma38; target=artI; function=+
- `activates` --> [[gene.b0864|gene.b0864]] `RegulonDB` `S` - sigma=sigma38; target=artP; function=+
- `activates` --> [[gene.b0865|gene.b0865]] `RegulonDB` `S` - sigma=sigma38; target=ybjP; function=+
- `activates` --> [[gene.b0871|gene.b0871]] `RegulonDB` `C` - sigma=sigma38; target=poxB; function=+
- `activates` --> [[gene.b0912|gene.b0912]] `RegulonDB` `S` - sigma=sigma38; target=ihfB; function=+
- `activates` --> [[gene.b0950|gene.b0950]] `RegulonDB` `S` - sigma=sigma38; target=pqiA; function=+
- `activates` --> [[gene.b0951|gene.b0951]] `RegulonDB` `S` - sigma=sigma38; target=pqiB; function=+
- `activates` --> [[gene.b0952|gene.b0952]] `RegulonDB` `S` - sigma=sigma38; target=pqiC; function=+
- `activates` --> [[gene.b0999|gene.b0999]] `RegulonDB` `S` - sigma=sigma38; target=cbpM; function=+
- `activates` --> [[gene.b1000|gene.b1000]] `RegulonDB` `S` - sigma=sigma38; target=cbpA; function=+
- `activates` --> [[gene.b1037|gene.b1037]] `RegulonDB` `S` - sigma=sigma38; target=csgG; function=+
- `activates` --> [[gene.b1038|gene.b1038]] `RegulonDB` `S` - sigma=sigma38; target=csgF; function=+
- `activates` --> [[gene.b1039|gene.b1039]] `RegulonDB` `S` - sigma=sigma38; target=csgE; function=+
- `activates` --> [[gene.b1040|gene.b1040]] `RegulonDB` `S` - sigma=sigma38; target=csgD; function=+
- `activates` --> [[gene.b1041|gene.b1041]] `RegulonDB` `C` - sigma=sigma38; target=csgB; function=+
- `activates` --> [[gene.b1042|gene.b1042]] `RegulonDB` `C` - sigma=sigma38; target=csgA; function=+
- `activates` --> [[gene.b1043|gene.b1043]] `RegulonDB` `C` - sigma=sigma38; target=csgC; function=+
- `activates` --> [[gene.b1051|gene.b1051]] `RegulonDB` `S` - sigma=sigma38; target=msyB; function=+
- `activates` --> [[gene.b1164|gene.b1164]] `RegulonDB` `S` - sigma=sigma38; target=ycgZ; function=+
- `activates` --> [[gene.b1165|gene.b1165]] `RegulonDB` `S` - sigma=sigma38; target=ymgA; function=+
- `activates` --> [[gene.b1166|gene.b1166]] `RegulonDB` `S` - sigma=sigma38; target=ariR; function=+
- `activates` --> [[gene.b1167|gene.b1167]] `RegulonDB` `S` - sigma=sigma38; target=ymgC; function=+
- `activates` --> [[gene.b1197|gene.b1197]] `RegulonDB` `S` - sigma=sigma38; target=treA; function=+
- `activates` --> [[gene.b1234|gene.b1234]] `RegulonDB` `S` - sigma=sigma38; target=rssA; function=+
- `activates` --> [[gene.b1235|gene.b1235]] `RegulonDB` `S` - sigma=sigma38; target=rssB; function=+
- `activates` --> [[gene.b1241|gene.b1241]] `RegulonDB` `S` - sigma=sigma38; target=adhE; function=+
- `activates` --> [[gene.b1274|gene.b1274]] `RegulonDB` `S` - sigma=sigma38; target=topA; function=+
- `activates` --> [[gene.b1276|gene.b1276]] `RegulonDB` `S` - sigma=sigma38; target=acnA; function=+
- `activates` --> [[gene.b1284|gene.b1284]] `RegulonDB` `S` - sigma=sigma38; target=yciT; function=+
- `activates` --> [[gene.b1285|gene.b1285]] `RegulonDB` `S` - sigma=sigma38; target=pdeR; function=+
- `activates` --> [[gene.b1453|gene.b1453]] `RegulonDB` `S` - sigma=sigma38; target=ansP; function=+
- `activates` --> [[gene.b1473|gene.b1473]] `RegulonDB` `S` - sigma=sigma38; target=yddG; function=+
- `activates` --> [[gene.b1480|gene.b1480]] `RegulonDB` `S` - sigma=sigma38; target=sra; function=+
- `activates` --> [[gene.b1492|gene.b1492]] `RegulonDB` `S` - sigma=sigma38; target=gadC; function=+
- `activates` --> [[gene.b1493|gene.b1493]] `RegulonDB` `S` - sigma=sigma38; target=gadB; function=+
- `activates` --> [[gene.b1587|gene.b1587]] `RegulonDB` `S` - sigma=sigma38; target=ynfE; function=+
- `activates` --> [[gene.b1588|gene.b1588]] `RegulonDB` `S` - sigma=sigma38; target=ynfF; function=+
- `activates` --> [[gene.b1589|gene.b1589]] `RegulonDB` `S` - sigma=sigma38; target=ynfG; function=+
- `activates` --> [[gene.b1590|gene.b1590]] `RegulonDB` `S` - sigma=sigma38; target=ynfH; function=+
- `activates` --> [[gene.b1591|gene.b1591]] `RegulonDB` `S` - sigma=sigma38; target=dmsD; function=+
- `activates` --> [[gene.b1597|gene.b1597]] `RegulonDB` `S` - sigma=sigma38; target=asr; function=+
- `activates` --> [[gene.b1611|gene.b1611]] `RegulonDB` `S` - sigma=sigma38; target=fumC; function=+
- `activates` --> [[gene.b1646|gene.b1646]] `RegulonDB` `S` - sigma=sigma38; target=sodC; function=+
- `activates` --> [[gene.b1669|gene.b1669]] `RegulonDB` `S` - sigma=sigma38; target=ydhT; function=+
- `activates` --> [[gene.b1670|gene.b1670]] `RegulonDB` `S` - sigma=sigma38; target=ydhU; function=+
- `activates` --> [[gene.b1671|gene.b1671]] `RegulonDB` `S` - sigma=sigma38; target=ydhX; function=+
- `activates` --> [[gene.b1672|gene.b1672]] `RegulonDB` `S` - sigma=sigma38; target=ydhW; function=+
- `activates` --> [[gene.b1673|gene.b1673]] `RegulonDB` `S` - sigma=sigma38; target=ydhV; function=+
- `activates` --> [[gene.b1674|gene.b1674]] `RegulonDB` `S` - sigma=sigma38; target=ydhY; function=+
- `activates` --> [[gene.b1712|gene.b1712]] `RegulonDB` `S` - sigma=sigma38; target=ihfA; function=+
- `activates` --> [[gene.b1723|gene.b1723]] `RegulonDB` `S` - sigma=sigma38; target=pfkB; function=+
- `activates` --> [[gene.b1732|gene.b1732]] `RegulonDB` `S` - sigma=sigma38; target=katE; function=+
- `activates` --> [[gene.b1739|gene.b1739]] `RegulonDB` `S` - sigma=sigma38; target=osmE; function=+
- `activates` --> [[gene.b1744|gene.b1744]] `RegulonDB` `C` - sigma=sigma38; target=astE; function=+
- `activates` --> [[gene.b1745|gene.b1745]] `RegulonDB` `C` - sigma=sigma38; target=astB; function=+
- `activates` --> [[gene.b1746|gene.b1746]] `RegulonDB` `C` - sigma=sigma38; target=astD; function=+
- `activates` --> [[gene.b1747|gene.b1747]] `RegulonDB` `C` - sigma=sigma38; target=astA; function=+
- `activates` --> [[gene.b1748|gene.b1748]] `RegulonDB` `C` - sigma=sigma38; target=astC; function=+
- `activates` --> [[gene.b1749|gene.b1749]] `RegulonDB` `S` - sigma=sigma38; target=xthA; function=+
- `activates` --> [[gene.b1779|gene.b1779]] `RegulonDB` `C` - sigma=sigma38; target=gapA; function=+
- `activates` --> [[gene.b1838|gene.b1838]] `RegulonDB` `S` - sigma=sigma38; target=pphA; function=+
- `activates` --> [[gene.b1896|gene.b1896]] `RegulonDB` `S` - sigma=sigma38; target=otsA; function=+
- `activates` --> [[gene.b1897|gene.b1897]] `RegulonDB` `S` - sigma=sigma38; target=otsB; function=+
- `activates` --> [[gene.b1900|gene.b1900]] `RegulonDB` `S` - sigma=sigma38; target=araG; function=+
- `activates` --> [[gene.b1901|gene.b1901]] `RegulonDB` `S` - sigma=sigma38; target=araF; function=+
- `activates` --> [[gene.b1967|gene.b1967]] `RegulonDB` `S` - sigma=sigma38; target=hchA; function=+
- `activates` --> [[gene.b2068|gene.b2068]] `RegulonDB` `S` - sigma=sigma38; target=alkA; function=+
- `activates` --> [[gene.b2097|gene.b2097]] `RegulonDB` `S` - sigma=sigma38; target=fbaB; function=+
- `activates` --> [[gene.b2127|gene.b2127]] `RegulonDB` `S` - sigma=sigma38; target=mlrA; function=+
- `activates` --> [[gene.b2128|gene.b2128]] `RegulonDB` `S` - sigma=sigma38; target=yehW; function=+
- `activates` --> [[gene.b2129|gene.b2129]] `RegulonDB` `S` - sigma=sigma38; target=yehX; function=+
- `activates` --> [[gene.b2130|gene.b2130]] `RegulonDB` `S` - sigma=sigma38; target=yehY; function=+
- `activates` --> [[gene.b2131|gene.b2131]] `RegulonDB` `S` - sigma=sigma38; target=osmF; function=+
- `activates` --> [[gene.b2212|gene.b2212]] `RegulonDB` `S` - sigma=sigma38; target=alkB; function=+
- `activates` --> [[gene.b2213|gene.b2213]] `RegulonDB` `S` - sigma=sigma38; target=ada; function=+
- `activates` --> [[gene.b2266|gene.b2266]] `RegulonDB` `S` - sigma=sigma38; target=elaB; function=+
- `activates` --> [[gene.b2344|gene.b2344]] `RegulonDB` `S` - sigma=sigma38; target=fadL; function=+
- `activates` --> [[gene.b2369|gene.b2369]] `RegulonDB` `S` - sigma=sigma38; target=evgA; function=+
- `activates` --> [[gene.b2370|gene.b2370]] `RegulonDB` `S` - sigma=sigma38; target=evgS; function=+
- `activates` --> [[gene.b2388|gene.b2388]] `RegulonDB` `S` - sigma=sigma38; target=glk; function=+
- `activates` --> [[gene.b2406|gene.b2406]] `RegulonDB` `S` - sigma=sigma38; target=xapB; function=+
- `activates` --> [[gene.b2407|gene.b2407]] `RegulonDB` `S` - sigma=sigma38; target=xapA; function=+
- `activates` --> [[gene.b2427|gene.b2427]] `RegulonDB` `S` - sigma=sigma38; target=murR; function=+
- `activates` --> [[gene.b2428|gene.b2428]] `RegulonDB` `S` - sigma=sigma38; target=murQ; function=+
- `activates` --> [[gene.b2429|gene.b2429]] `RegulonDB` `S` - sigma=sigma38; target=murP; function=+
- `activates` --> [[gene.b2464|gene.b2464]] `RegulonDB` `S` - sigma=sigma38; target=talA; function=+
- `activates` --> [[gene.b2465|gene.b2465]] `RegulonDB` `S` - sigma=sigma38; target=tktB; function=+
- `activates` --> [[gene.b2535|gene.b2535]] `RegulonDB` `S` - sigma=sigma38; target=csiE; function=+
- `activates` --> [[gene.b2552|gene.b2552]] `RegulonDB` `C` - sigma=sigma38; target=hmp; function=+
- `activates` --> [[gene.b2570|gene.b2570]] `RegulonDB` `S` - sigma=sigma38; target=rseC; function=+
- `activates` --> [[gene.b2571|gene.b2571]] `RegulonDB` `S` - sigma=sigma38; target=rseB; function=+
- `activates` --> [[gene.b2572|gene.b2572]] `RegulonDB` `S` - sigma=sigma38; target=rseA; function=+
- `activates` --> [[gene.b2573|gene.b2573]] `RegulonDB` `S` - sigma=sigma38; target=rpoE; function=+
- `activates` --> [[gene.b2677|gene.b2677]] `RegulonDB` `S` - sigma=sigma38; target=proV; function=+
- `activates` --> [[gene.b2678|gene.b2678]] `RegulonDB` `S` - sigma=sigma38; target=proW; function=+
- `activates` --> [[gene.b2679|gene.b2679]] `RegulonDB` `S` - sigma=sigma38; target=proX; function=+
- `activates` --> [[gene.b2687|gene.b2687]] `RegulonDB` `S` - sigma=sigma38; target=luxS; function=+
- `activates` --> [[gene.b2696|gene.b2696]] `RegulonDB` `S` - sigma=sigma38; target=csrA; function=+
- `activates` --> [[gene.b2733|gene.b2733]] `RegulonDB` `S` - sigma=sigma38; target=mutS; function=+
- `activates` --> [[gene.b2911|gene.b2911]] `RegulonDB` `S` - sigma=sigma38; target=ssrS; function=+
- `activates` --> [[gene.b2912|gene.b2912]] `RegulonDB` `S` - sigma=sigma38; target=fau; function=+
- `activates` --> [[gene.b2922|gene.b2922]] `RegulonDB` `S` - sigma=sigma38; target=yggE; function=+
- `activates` --> [[gene.b2925|gene.b2925]] `RegulonDB` `C` - sigma=sigma38; target=fbaA; function=+
- `activates` --> [[gene.b2926|gene.b2926]] `RegulonDB` `C` - sigma=sigma38; target=pgk; function=+
- `activates` --> [[gene.b2927|gene.b2927]] `RegulonDB` `C` - sigma=sigma38; target=epd; function=+
- `activates` --> [[gene.b2937|gene.b2937]] `RegulonDB` `S` - sigma=sigma38; target=speB; function=+
- `activates` --> [[gene.b2942|gene.b2942]] `RegulonDB` `S` - sigma=sigma38; target=metK; function=+
- `activates` --> [[gene.b3035|gene.b3035]] `RegulonDB` `S` - sigma=sigma38; target=tolC; function=+
- `activates` --> [[gene.b3037|gene.b3037]] `RegulonDB` `S` - sigma=sigma38; target=ygiB; function=+
- `activates` --> [[gene.b3038|gene.b3038]] `RegulonDB` `S` - sigma=sigma38; target=ygiC; function=+
- `activates` --> [[gene.b3049|gene.b3049]] `RegulonDB` `S` - sigma=sigma38; target=glgS; function=+
- `activates` --> [[gene.b3073|gene.b3073]] `RegulonDB` `S` - sigma=sigma38; target=patA; function=+
- `activates` --> [[gene.b3212|gene.b3212]] `RegulonDB` `S` - sigma=sigma38; target=gltB; function=+
- `activates` --> [[gene.b3213|gene.b3213]] `RegulonDB` `S` - sigma=sigma38; target=gltD; function=+
- `activates` --> [[gene.b3214|gene.b3214]] `RegulonDB` `S` - sigma=sigma38; target=gltF; function=+
- `activates` --> [[gene.b3360|gene.b3360]] `RegulonDB` `C` - sigma=sigma38; target=pabA; function=+
- `activates` --> [[gene.b3361|gene.b3361]] `RegulonDB` `C` - sigma=sigma38; target=fic; function=+
- `activates` --> [[gene.b3362|gene.b3362]] `RegulonDB` `C` - sigma=sigma38; target=yhfG; function=+
- `activates` --> [[gene.b3428|gene.b3428]] `RegulonDB` `S` - sigma=sigma38; target=glgP; function=+
- `activates` --> [[gene.b3429|gene.b3429]] `RegulonDB` `S` - sigma=sigma38; target=glgA; function=+
- `activates` --> [[gene.b3430|gene.b3430]] `RegulonDB` `S` - sigma=sigma38; target=glgC; function=+
- `activates` --> [[gene.b3461|gene.b3461]] `RegulonDB` `S` - sigma=sigma38; target=rpoH; function=+
- `activates` --> [[gene.b3494|gene.b3494]] `RegulonDB` `S` - sigma=sigma38; target=uspB; function=+
- `activates` --> [[gene.b3508|gene.b3508]] `RegulonDB` `S` - sigma=sigma38; target=yhiD; function=+
- `activates` --> [[gene.b3509|gene.b3509]] `RegulonDB` `S` - sigma=sigma38; target=hdeB; function=+
- `activates` --> [[gene.b3510|gene.b3510]] `RegulonDB` `S` - sigma=sigma38; target=hdeA; function=+
- `activates` --> [[gene.b3511|gene.b3511]] `RegulonDB` `S` - sigma=sigma38; target=hdeD; function=+
- `activates` --> [[gene.b3512|gene.b3512]] `RegulonDB` `S` - sigma=sigma38; target=gadE; function=+
- `activates` --> [[gene.b3513|gene.b3513]] `RegulonDB` `S` - sigma=sigma38; target=mdtE; function=+
- `activates` --> [[gene.b3514|gene.b3514]] `RegulonDB` `S` - sigma=sigma38; target=mdtF; function=+
- `activates` --> [[gene.b3517|gene.b3517]] `RegulonDB` `S` - sigma=sigma38; target=gadA; function=+
- `activates` --> [[gene.b3555|gene.b3555]] `RegulonDB` `S` - sigma=sigma38; target=yiaG; function=+
- `activates` --> [[gene.b3700|gene.b3700]] `RegulonDB` `S` - sigma=sigma38; target=recF; function=+
- `activates` --> [[gene.b3701|gene.b3701]] `RegulonDB` `S` - sigma=sigma38; target=dnaN; function=+
- `activates` --> [[gene.b3724|gene.b3724]] `RegulonDB` `S` - sigma=sigma38; target=phoU; function=+
- `activates` --> [[gene.b3725|gene.b3725]] `RegulonDB` `S` - sigma=sigma38; target=pstB; function=+
- `activates` --> [[gene.b3726|gene.b3726]] `RegulonDB` `S` - sigma=sigma38; target=pstA; function=+
- `activates` --> [[gene.b3727|gene.b3727]] `RegulonDB` `S` - sigma=sigma38; target=pstC; function=+
- `activates` --> [[gene.b3728|gene.b3728]] `RegulonDB` `S` - sigma=sigma38; target=pstS; function=+
- `activates` --> [[gene.b3740|gene.b3740]] `RegulonDB` `S` - sigma=sigma38; target=rsmG; function=+
- `activates` --> [[gene.b3741|gene.b3741]] `RegulonDB` `S` - sigma=sigma38; target=mnmG; function=+
- `activates` --> [[gene.b3773|gene.b3773]] `RegulonDB` `S` - sigma=sigma38; target=ilvY; function=+
- `activates` --> [[gene.b3862|gene.b3862]] `RegulonDB` `S` - sigma=sigma38; target=yihG; function=+
- `activates` --> [[gene.b3905|gene.b3905]] `RegulonDB` `S` - sigma=sigma38; target=rhaS; function=+
- `activates` --> [[gene.b3906|gene.b3906]] `RegulonDB` `S` - sigma=sigma38; target=rhaR; function=+
- `activates` --> [[gene.b3916|gene.b3916]] `RegulonDB` `S` - sigma=sigma38; target=pfkA; function=+
- `activates` --> [[gene.b3929|gene.b3929]] `RegulonDB` `S` - sigma=sigma38; target=rraA; function=+
- `activates` --> [[gene.b3961|gene.b3961]] `RegulonDB` `S` - sigma=sigma38; target=oxyR; function=+
- `activates` --> [[gene.b3995|gene.b3995]] `RegulonDB` `S` - sigma=sigma38; target=rsd; function=+
- `activates` --> [[gene.b4025|gene.b4025]] `RegulonDB` `C` - sigma=sigma38; target=pgi; function=+
- `activates` --> [[gene.b4067|gene.b4067]] `RegulonDB` `S` - sigma=sigma38; target=actP; function=+
- `activates` --> [[gene.b4068|gene.b4068]] `RegulonDB` `S` - sigma=sigma38; target=yjcH; function=+
- `activates` --> [[gene.b4069|gene.b4069]] `RegulonDB` `S` - sigma=sigma38; target=acs; function=+
- `activates` --> [[gene.b4111|gene.b4111]] `RegulonDB` `S` - sigma=sigma38; target=proP; function=+
- `activates` --> [[gene.b4149|gene.b4149]] `RegulonDB` `S` - sigma=sigma38; target=blc; function=+
- `activates` --> [[gene.b4151|gene.b4151]] `RegulonDB` `S` - sigma=sigma38; target=frdD; function=+
- `activates` --> [[gene.b4152|gene.b4152]] `RegulonDB` `S` - sigma=sigma38; target=frdC; function=+
- `activates` --> [[gene.b4153|gene.b4153]] `RegulonDB` `S` - sigma=sigma38; target=frdB; function=+
- `activates` --> [[gene.b4154|gene.b4154]] `RegulonDB` `S` - sigma=sigma38; target=frdA; function=+
- `activates` --> [[gene.b4187|gene.b4187]] `RegulonDB` `S` - sigma=sigma38; target=aidB; function=+
- `activates` --> [[gene.b4217|gene.b4217]] `RegulonDB` `S` - sigma=sigma38; target=ytfK; function=+
- `activates` --> [[gene.b4354|gene.b4354]] `RegulonDB` `S` - sigma=sigma38; target=btsT; function=+
- `activates` --> [[gene.b4376|gene.b4376]] `RegulonDB` `S` - sigma=sigma38; target=osmY; function=+
- `activates` --> [[gene.b4409|gene.b4409]] `RegulonDB` `S` - sigma=sigma38; target=blr; function=+
- `activates` --> [[gene.b4411|gene.b4411]] `RegulonDB` `S` - sigma=sigma38; target=ecnB; function=+
- `activates` --> [[gene.b4433|gene.b4433]] `RegulonDB` `S` - sigma=sigma38; target=sdsR; function=+
- `activates` --> [[gene.b4438|gene.b4438]] `RegulonDB` `C` - sigma=sigma38; target=cyaR; function=+
- `activates` --> [[gene.b4439|gene.b4439]] `RegulonDB` `S` - sigma=sigma38; target=micF; function=+
- `activates` --> [[gene.b4452|gene.b4452]] `RegulonDB` `S` - sigma=sigma38; target=gadY; function=+
- `activates` --> [[gene.b4459|gene.b4459]] `RegulonDB` `S` - sigma=sigma38; target=ryjA; function=+
- `activates` --> [[gene.b4460|gene.b4460]] `RegulonDB` `S` - sigma=sigma38; target=araH; function=+
- `activates` --> [[gene.b4577|gene.b4577]] `RegulonDB` `S` - sigma=sigma38; target=sgrS; function=+
- `activates` --> [[gene.b4596|gene.b4596]] `RegulonDB` `S` - sigma=sigma38; target=yciZ; function=+
- `activates` --> [[gene.b4662|gene.b4662]] `RegulonDB` `S` - sigma=sigma38; target=sgrT; function=+
- `activates` --> [[gene.b4718|gene.b4718]] `RegulonDB` `S` - sigma=sigma38; target=gadF; function=+
- `activates` --> [[gene.b4719|gene.b4719]] `RegulonDB` `S` - sigma=sigma38; target=sdsN; function=+
- `activates` --> [[gene.b4725|gene.b4725]] `RegulonDB` `S` - sigma=sigma38; target=rseD; function=+
- `activates` --> [[gene.b4741|gene.b4741]] `RegulonDB` `S` - sigma=sigma38; target=ymiC; function=+
- `activates` --> [[gene.b4764|gene.b4764]] `RegulonDB` `S` - sigma=sigma38; target=sdhX; function=+
- `activates` --> [[gene.b4781|gene.b4781]] `RegulonDB` `S` - sigma=sigma38; target=evgL; function=+
- `is_component_of` --> [[complex.ecocyc.RNAPS-CPLX|complex.ecocyc.RNAPS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2741|gene.b2741]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P13445`
- `KEGG:ecj:JW5437;eco:b2741;ecoc:C3026_15075;`
- `GeneID:947210;`
- `GO:GO:0000345; GO:0000976; GO:0001000; GO:0003899; GO:0005737; GO:0006352; GO:0006355; GO:0006950; GO:0016987; GO:0045892; GO:1903865; GO:2000142`

## Notes

RNA polymerase sigma factor RpoS (Sigma S) (Sigma-38)
