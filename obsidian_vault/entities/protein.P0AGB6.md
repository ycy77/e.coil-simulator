---
entity_id: "protein.P0AGB6"
entity_type: "protein"
name: "rpoE"
source_database: "UniProt"
source_id: "P0AGB6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:11777003, ECO:0000269|PubMed:9159522}. Note=Associates with the inner membrane via RseA (PubMed:11777003, PubMed:9159522). {ECO:0000269|PubMed:11777003}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpoE sigE b2573 JW2557"
---

# rpoE

`protein.P0AGB6`

## Static

- Type: `protein`
- Source: `UniProt:P0AGB6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:11777003, ECO:0000269|PubMed:9159522}. Note=Associates with the inner membrane via RseA (PubMed:11777003, PubMed:9159522). {ECO:0000269|PubMed:11777003}.

## Enriched Summary

FUNCTION: Sigma factors are initiation factors that promote the attachment of RNA polymerase (RNAP) to specific initiation sites and are then released (PubMed:2691330, PubMed:7889935, PubMed:9159522, PubMed:9159523). Extracytoplasmic function (ECF) sigma-E controls the envelope stress response, responding to periplasmic protein stress, increased levels of periplasmic lipopolysaccharide (LPS) as well as heat shock (PubMed:7889935) and oxidative stress; it controls protein processing in the extracytoplasmic compartment. The 90 member regulon consists of the genes necessary for the synthesis and maintenance of both proteins and LPS of the outer membrane (PubMed:11274153, PubMed:16336047, PubMed:7889934). Indirectly activates transcription of csrB and csrC, 2 sRNAs that antagonize translational regulator CsrA, linking envelope stress, the stringent response and the catabolite repression systems (PubMed:28924029). {ECO:0000269|PubMed:11274153, ECO:0000269|PubMed:16336047, ECO:0000269|PubMed:2691330, ECO:0000269|PubMed:28924029, ECO:0000269|PubMed:7889934, ECO:0000269|PubMed:7889935, ECO:0000269|PubMed:9159522, ECO:0000269|PubMed:9159523}. Sigma E is a minor sigma factor, specializing in responses to the effects of heat shock and other stresses on membrane and periplasmic proteins. It is regulated by a multistep protease system that sense disruptions in those proteins...

## Biological Role

Component of RNA polymerase sigma 24 (complex.ecocyc.RNAPE-CPLX).

## Annotation

FUNCTION: Sigma factors are initiation factors that promote the attachment of RNA polymerase (RNAP) to specific initiation sites and are then released (PubMed:2691330, PubMed:7889935, PubMed:9159522, PubMed:9159523). Extracytoplasmic function (ECF) sigma-E controls the envelope stress response, responding to periplasmic protein stress, increased levels of periplasmic lipopolysaccharide (LPS) as well as heat shock (PubMed:7889935) and oxidative stress; it controls protein processing in the extracytoplasmic compartment. The 90 member regulon consists of the genes necessary for the synthesis and maintenance of both proteins and LPS of the outer membrane (PubMed:11274153, PubMed:16336047, PubMed:7889934). Indirectly activates transcription of csrB and csrC, 2 sRNAs that antagonize translational regulator CsrA, linking envelope stress, the stringent response and the catabolite repression systems (PubMed:28924029). {ECO:0000269|PubMed:11274153, ECO:0000269|PubMed:16336047, ECO:0000269|PubMed:2691330, ECO:0000269|PubMed:28924029, ECO:0000269|PubMed:7889934, ECO:0000269|PubMed:7889935, ECO:0000269|PubMed:9159522, ECO:0000269|PubMed:9159523}.

## Outgoing Edges (113)

- `activates` --> [[gene.b0054|gene.b0054]] `RegulonDB` `S` - sigma=sigma24; target=lptD; function=+
- `activates` --> [[gene.b0161|gene.b0161]] `RegulonDB` `S` - sigma=sigma24; target=degP; function=+
- `activates` --> [[gene.b0176|gene.b0176]] `RegulonDB` `S` - sigma=sigma24; target=rseP; function=+
- `activates` --> [[gene.b0177|gene.b0177]] `RegulonDB` `S` - sigma=sigma24; target=bamA; function=+
- `activates` --> [[gene.b0178|gene.b0178]] `RegulonDB` `S` - sigma=sigma24; target=skp; function=+
- `activates` --> [[gene.b0179|gene.b0179]] `RegulonDB` `S` - sigma=sigma24; target=lpxD; function=+
- `activates` --> [[gene.b0180|gene.b0180]] `RegulonDB` `S` - sigma=sigma24; target=fabZ; function=+
- `activates` --> [[gene.b0181|gene.b0181]] `RegulonDB` `S` - sigma=sigma24; target=lpxA; function=+
- `activates` --> [[gene.b0182|gene.b0182]] `RegulonDB` `S` - sigma=sigma24; target=lpxB; function=+
- `activates` --> [[gene.b0183|gene.b0183]] `RegulonDB` `S` - sigma=sigma24; target=rnhB; function=+
- `activates` --> [[gene.b0184|gene.b0184]] `RegulonDB` `S` - sigma=sigma24; target=dnaE; function=+
- `activates` --> [[gene.b0377|gene.b0377]] `RegulonDB` `S` - sigma=sigma24; target=sbmA; function=+
- `activates` --> [[gene.b0378|gene.b0378]] `RegulonDB` `S` - sigma=sigma24; target=yaiW; function=+
- `activates` --> [[gene.b0438|gene.b0438]] `RegulonDB` `S` - sigma=sigma24; target=clpX; function=+
- `activates` --> [[gene.b0439|gene.b0439]] `RegulonDB` `S` - sigma=sigma24; target=lon; function=+
- `activates` --> [[gene.b0471|gene.b0471]] `RegulonDB` `S` - sigma=sigma24; target=ybaB; function=+
- `activates` --> [[gene.b0472|gene.b0472]] `RegulonDB` `S` - sigma=sigma24; target=recR; function=+
- `activates` --> [[gene.b0554|gene.b0554]] `RegulonDB` `S` - sigma=sigma24; target=essD; function=+
- `activates` --> [[gene.b0555|gene.b0555]] `RegulonDB` `S` - sigma=sigma24; target=rrrD; function=+
- `activates` --> [[gene.b0556|gene.b0556]] `RegulonDB` `S` - sigma=sigma24; target=rzpD; function=+
- `activates` --> [[gene.b0606|gene.b0606]] `RegulonDB` `S` - sigma=sigma24; target=ahpF; function=+
- `activates` --> [[gene.b0872|gene.b0872]] `RegulonDB` `S` - sigma=sigma24; target=hcr; function=+
- `activates` --> [[gene.b0873|gene.b0873]] `RegulonDB` `S` - sigma=sigma24; target=hcp; function=+
- `activates` --> [[gene.b1013|gene.b1013]] `RegulonDB` `S` - sigma=sigma24; target=rutR; function=+
- `activates` --> [[gene.b1048|gene.b1048]] `RegulonDB` `S` - sigma=sigma24; target=opgG; function=+
- `activates` --> [[gene.b1049|gene.b1049]] `RegulonDB` `S` - sigma=sigma24; target=opgH; function=+
- `activates` --> [[gene.b1465|gene.b1465]] `RegulonDB` `S` - sigma=sigma24; target=narV; function=+
- `activates` --> [[gene.b1466|gene.b1466]] `RegulonDB` `S` - sigma=sigma24; target=narW; function=+
- `activates` --> [[gene.b1643|gene.b1643]] `RegulonDB` `S` - sigma=sigma24; target=ydhI; function=+
- `activates` --> [[gene.b1644|gene.b1644]] `RegulonDB` `S` - sigma=sigma24; target=ydhJ; function=+
- `activates` --> [[gene.b1645|gene.b1645]] `RegulonDB` `S` - sigma=sigma24; target=ydhK; function=+
- `activates` --> [[gene.b1653|gene.b1653]] `RegulonDB` `S` - sigma=sigma24; target=lhr; function=+
- `activates` --> [[gene.b1806|gene.b1806]] `RegulonDB` `S` - sigma=sigma24; target=yeaY; function=+
- `activates` --> [[gene.b1902|gene.b1902]] `RegulonDB` `S` - sigma=sigma24; target=ftnB; function=+
- `activates` --> [[gene.b2060|gene.b2060]] `RegulonDB` `S` - sigma=sigma24; target=wzc; function=+
- `activates` --> [[gene.b2061|gene.b2061]] `RegulonDB` `S` - sigma=sigma24; target=wzb; function=+
- `activates` --> [[gene.b2062|gene.b2062]] `RegulonDB` `S` - sigma=sigma24; target=wza; function=+
- `activates` --> [[gene.b2340|gene.b2340]] `RegulonDB` `S` - sigma=sigma24; target=sixA; function=+
- `activates` --> [[gene.b2378|gene.b2378]] `RegulonDB` `S` - sigma=sigma24; target=lpxP; function=+
- `activates` --> [[gene.b2419|gene.b2419]] `RegulonDB` `S` - sigma=sigma24; target=yfeK; function=+
- `activates` --> [[gene.b2420|gene.b2420]] `RegulonDB` `S` - sigma=sigma24; target=yfeS; function=+
- `activates` --> [[gene.b2431|gene.b2431]] `RegulonDB` `S` - sigma=sigma24; target=yfeX; function=+
- `activates` --> [[gene.b2432|gene.b2432]] `RegulonDB` `S` - sigma=sigma24; target=yfeY; function=+
- `activates` --> [[gene.b2477|gene.b2477]] `RegulonDB` `S` - sigma=sigma24; target=bamC; function=+
- `activates` --> [[gene.b2494|gene.b2494]] `RegulonDB` `S` - sigma=sigma24; target=bepA; function=+
- `activates` --> [[gene.b2495|gene.b2495]] `RegulonDB` `S` - sigma=sigma24; target=yfgD; function=+
- `activates` --> [[gene.b2511|gene.b2511]] `RegulonDB` `S` - sigma=sigma24; target=der; function=+
- `activates` --> [[gene.b2512|gene.b2512]] `RegulonDB` `S` - sigma=sigma24; target=bamB; function=+
- `activates` --> [[gene.b2570|gene.b2570]] `RegulonDB` `S` - sigma=sigma24; target=rseC; function=+
- `activates` --> [[gene.b2571|gene.b2571]] `RegulonDB` `S` - sigma=sigma24; target=rseB; function=+
- `activates` --> [[gene.b2572|gene.b2572]] `RegulonDB` `S` - sigma=sigma24; target=rseA; function=+
- `activates` --> [[gene.b2573|gene.b2573]] `RegulonDB` `S` - sigma=sigma24; target=rpoE; function=+
- `activates` --> [[gene.b2595|gene.b2595]] `RegulonDB` `S` - sigma=sigma24; target=bamD; function=+
- `activates` --> [[gene.b2617|gene.b2617]] `RegulonDB` `S` - sigma=sigma24; target=bamE; function=+
- `activates` --> [[gene.b2631|gene.b2631]] `RegulonDB` `S` - sigma=sigma24; target=rnlB; function=+
- `activates` --> [[gene.b2891|gene.b2891]] `RegulonDB` `S` - sigma=sigma24; target=prfB; function=+
- `activates` --> [[gene.b2892|gene.b2892]] `RegulonDB` `S` - sigma=sigma24; target=recJ; function=+
- `activates` --> [[gene.b2893|gene.b2893]] `RegulonDB` `S` - sigma=sigma24; target=dsbC; function=+
- `activates` --> [[gene.b2958|gene.b2958]] `RegulonDB` `S` - sigma=sigma24; target=yggN; function=+
- `activates` --> [[gene.b2970|gene.b2970]] `RegulonDB` `S` - sigma=sigma24; target=yghF; function=+
- `activates` --> [[gene.b3055|gene.b3055]] `RegulonDB` `S` - sigma=sigma24; target=ygiM; function=+
- `activates` --> [[gene.b3056|gene.b3056]] `RegulonDB` `S` - sigma=sigma24; target=cca; function=+
- `activates` --> [[gene.b3057|gene.b3057]] `RegulonDB` `S` - sigma=sigma24; target=bacA; function=+
- `activates` --> [[gene.b3067|gene.b3067]] `RegulonDB` `S` - sigma=sigma24; target=rpoD; function=+
- `activates` --> [[gene.b3095|gene.b3095]] `RegulonDB` `S` - sigma=sigma24; target=yqjA; function=+
- `activates` --> [[gene.b3096|gene.b3096]] `RegulonDB` `S` - sigma=sigma24; target=mzrA; function=+
- `activates` --> [[gene.b3150|gene.b3150]] `RegulonDB` `S` - sigma=sigma24; target=dolP; function=+
- `activates` --> [[gene.b3181|gene.b3181]] `RegulonDB` `S` - sigma=sigma24; target=greA; function=+
- `activates` --> [[gene.b3200|gene.b3200]] `RegulonDB` `S` - sigma=sigma24; target=lptA; function=+
- `activates` --> [[gene.b3201|gene.b3201]] `RegulonDB` `S` - sigma=sigma24; target=lptB; function=+
- `activates` --> [[gene.b3202|gene.b3202]] `RegulonDB` `S` - sigma=sigma24; target=rpoN; function=+
- `activates` --> [[gene.b3203|gene.b3203]] `RegulonDB` `S` - sigma=sigma24; target=hpf; function=+
- `activates` --> [[gene.b3204|gene.b3204]] `RegulonDB` `S` - sigma=sigma24; target=ptsN; function=+
- `activates` --> [[gene.b3205|gene.b3205]] `RegulonDB` `S` - sigma=sigma24; target=rapZ; function=+
- `activates` --> [[gene.b3206|gene.b3206]] `RegulonDB` `S` - sigma=sigma24; target=npr; function=+
- `activates` --> [[gene.b3322|gene.b3322]] `RegulonDB` `S` - sigma=sigma24; target=gspB; function=+
- `activates` --> [[gene.b3323|gene.b3323]] `RegulonDB` `S` - sigma=sigma24; target=gspA; function=+
- `activates` --> [[gene.b3339|gene.b3339]] `RegulonDB` `S` - sigma=sigma24; target=tufA; function=+
- `activates` --> [[gene.b3340|gene.b3340]] `RegulonDB` `S` - sigma=sigma24; target=fusA; function=+
- `activates` --> [[gene.b3347|gene.b3347]] `RegulonDB` `S` - sigma=sigma24; target=fkpA; function=+
- `activates` --> [[gene.b3416|gene.b3416]] `RegulonDB` `S` - sigma=sigma24; target=malQ; function=+
- `activates` --> [[gene.b3461|gene.b3461]] `RegulonDB` `S` - sigma=sigma24; target=rpoH; function=+
- `activates` --> [[gene.b3527|gene.b3527]] `RegulonDB` `S` - sigma=sigma24; target=bipP; function=+
- `activates` --> [[gene.b3546|gene.b3546]] `RegulonDB` `S` - sigma=sigma24; target=eptB; function=+
- `activates` --> [[gene.b3575|gene.b3575]] `RegulonDB` `S` - sigma=sigma24; target=yiaK; function=+
- `activates` --> [[gene.b3576|gene.b3576]] `RegulonDB` `S` - sigma=sigma24; target=yiaL; function=+
- `activates` --> [[gene.b3577|gene.b3577]] `RegulonDB` `S` - sigma=sigma24; target=yiaM; function=+
- `activates` --> [[gene.b3578|gene.b3578]] `RegulonDB` `S` - sigma=sigma24; target=yiaN; function=+
- `activates` --> [[gene.b3579|gene.b3579]] `RegulonDB` `S` - sigma=sigma24; target=yiaO; function=+
- `activates` --> [[gene.b3580|gene.b3580]] `RegulonDB` `S` - sigma=sigma24; target=lyxK; function=+
- `activates` --> [[gene.b3581|gene.b3581]] `RegulonDB` `S` - sigma=sigma24; target=sgbH; function=+
- `activates` --> [[gene.b3582|gene.b3582]] `RegulonDB` `S` - sigma=sigma24; target=sgbU; function=+
- `activates` --> [[gene.b3583|gene.b3583]] `RegulonDB` `S` - sigma=sigma24; target=sgbE; function=+
- `activates` --> [[gene.b3619|gene.b3619]] `RegulonDB` `S` - sigma=sigma24; target=rfaD; function=+
- `activates` --> [[gene.b3620|gene.b3620]] `RegulonDB` `S` - sigma=sigma24; target=waaF; function=+
- `activates` --> [[gene.b3621|gene.b3621]] `RegulonDB` `S` - sigma=sigma24; target=waaC; function=+
- `activates` --> [[gene.b3622|gene.b3622]] `RegulonDB` `S` - sigma=sigma24; target=waaL; function=+
- `activates` --> [[gene.b3656|gene.b3656]] `RegulonDB` `S` - sigma=sigma24; target=yicI; function=+
- `activates` --> [[gene.b3657|gene.b3657]] `RegulonDB` `S` - sigma=sigma24; target=yicJ; function=+
- `activates` --> [[gene.b3688|gene.b3688]] `RegulonDB` `S` - sigma=sigma24; target=yidQ; function=+
- `activates` --> [[gene.b3712|gene.b3712]] `RegulonDB` `S` - sigma=sigma24; target=yieE; function=+
- `activates` --> [[gene.b3713|gene.b3713]] `RegulonDB` `S` - sigma=sigma24; target=yieF; function=+
- `activates` --> [[gene.b3922|gene.b3922]] `RegulonDB` `S` - sigma=sigma24; target=yiiS; function=+
- `activates` --> [[gene.b3923|gene.b3923]] `RegulonDB` `S` - sigma=sigma24; target=uspD; function=+
- `activates` --> [[gene.b4041|gene.b4041]] `RegulonDB` `S` - sigma=sigma24; target=plsB; function=+
- `activates` --> [[gene.b4159|gene.b4159]] `RegulonDB` `S` - sigma=sigma24; target=mscM; function=+
- `activates` --> [[gene.b4160|gene.b4160]] `RegulonDB` `S` - sigma=sigma24; target=psd; function=+
- `activates` --> [[gene.b4216|gene.b4216]] `RegulonDB` `S` - sigma=sigma24; target=ytfJ; function=+
- `activates` --> [[gene.b4417|gene.b4417]] `RegulonDB` `S` - sigma=sigma24; target=rybB; function=+
- `activates` --> [[gene.b4438|gene.b4438]] `RegulonDB` `C` - sigma=sigma24; target=cyaR; function=+
- `activates` --> [[gene.b4442|gene.b4442]] `RegulonDB` `S` - sigma=sigma24; target=micA; function=+
- `activates` --> [[gene.b4717|gene.b4717]] `RegulonDB` `S` - sigma=sigma24; target=micL; function=+
- `is_component_of` --> [[complex.ecocyc.RNAPE-CPLX|complex.ecocyc.RNAPE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2573|gene.b2573]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGB6`
- `KEGG:ecj:JW2557;eco:b2573;ecoc:C3026_14250;`
- `GeneID:86860694;93774518;947050;`
- `GO:GO:0000345; GO:0003677; GO:0005737; GO:0005886; GO:0006352; GO:0006355; GO:0006970; GO:0009266; GO:0016987; GO:0036460; GO:0045892; GO:0090605; GO:1903865; GO:2000142`

## Notes

ECF RNA polymerase sigma-E factor (RNA polymerase sigma-E factor) (Sigma-24)
