---
entity_id: "protein.P0AGB3"
entity_type: "protein"
name: "rpoH"
source_database: "UniProt"
source_id: "P0AGB3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00961}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpoH fam hin htpR b3461 JW3426"
---

# rpoH

`protein.P0AGB3`

## Static

- Type: `protein`
- Source: `UniProt:P0AGB3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00961}.

## Enriched Summary

FUNCTION: Sigma factors are initiation factors that promote the attachment of RNA polymerase to specific initiation sites and are then released. This sigma factor is involved in regulation of expression of heat shock genes. Intracellular concentration of free RpoH protein increases in response to heat shock, which causes association with RNA polymerase (RNAP) and initiation of transcription of heat shock genes, including numerous global transcriptional regulators and genes involved in maintaining membrane functionality and homeostasis. RpoH is then quickly degraded, leading to a decrease in the rate of synthesis of heat shock proteins and shut-off of the heat shock response. {ECO:0000255|HAMAP-Rule:MF_00961, ECO:0000269|PubMed:15757896, ECO:0000269|PubMed:16818608, ECO:0000269|PubMed:3306410, ECO:0000269|PubMed:3315848, ECO:0000269|PubMed:6387714}. rpoH encodes σ32, the primary sigma factor controlling the heat shock response during log-phase growth. It is subject to tight control via a multivalent regulatory system that reponds to temperature and the abundance of misfolded proteins within the cell. σ32 levels rise, plateau and then drop following a heat shock, causing a similar induction in expression in heat shock genes . At elevated temperatures, formation of Eσ32 is favoured over that of Eσ70; σ32 has greater affinity for APORNAP-CPLX than σ70 at high temperatures...

## Biological Role

Component of RNA polymerase sigma 32 (complex.ecocyc.RNAP32-CPLX).

## Annotation

FUNCTION: Sigma factors are initiation factors that promote the attachment of RNA polymerase to specific initiation sites and are then released. This sigma factor is involved in regulation of expression of heat shock genes. Intracellular concentration of free RpoH protein increases in response to heat shock, which causes association with RNA polymerase (RNAP) and initiation of transcription of heat shock genes, including numerous global transcriptional regulators and genes involved in maintaining membrane functionality and homeostasis. RpoH is then quickly degraded, leading to a decrease in the rate of synthesis of heat shock proteins and shut-off of the heat shock response. {ECO:0000255|HAMAP-Rule:MF_00961, ECO:0000269|PubMed:15757896, ECO:0000269|PubMed:16818608, ECO:0000269|PubMed:3306410, ECO:0000269|PubMed:3315848, ECO:0000269|PubMed:6387714}.

## Outgoing Edges (100)

- `activates` --> [[gene.b0012|gene.b0012]] `RegulonDB` `S` - sigma=sigma32; target=mbiA; function=+
- `activates` --> [[gene.b0014|gene.b0014]] `RegulonDB` `S` - sigma=sigma32; target=dnaK; function=+
- `activates` --> [[gene.b0015|gene.b0015]] `RegulonDB` `S` - sigma=sigma32; target=dnaJ; function=+
- `activates` --> [[gene.b0026|gene.b0026]] `RegulonDB` `S` - sigma=sigma32; target=ileS; function=+
- `activates` --> [[gene.b0027|gene.b0027]] `RegulonDB` `S` - sigma=sigma32; target=lspA; function=+
- `activates` --> [[gene.b0028|gene.b0028]] `RegulonDB` `S` - sigma=sigma32; target=fkpB; function=+
- `activates` --> [[gene.b0029|gene.b0029]] `RegulonDB` `S` - sigma=sigma32; target=ispH; function=+
- `activates` --> [[gene.b0059|gene.b0059]] `RegulonDB` `S` - sigma=sigma32; target=rapA; function=+
- `activates` --> [[gene.b0126|gene.b0126]] `RegulonDB` `S` - sigma=sigma32; target=can; function=+
- `activates` --> [[gene.b0201|gene.b0201]] `RegulonDB` `S` - sigma=sigma32; target=rrsH; function=+
- `activates` --> [[gene.b0202|gene.b0202]] `RegulonDB` `S` - sigma=sigma32; target=ileV; function=+
- `activates` --> [[gene.b0203|gene.b0203]] `RegulonDB` `S` - sigma=sigma32; target=alaV; function=+
- `activates` --> [[gene.b0204|gene.b0204]] `RegulonDB` `S` - sigma=sigma32; target=rrlH; function=+
- `activates` --> [[gene.b0205|gene.b0205]] `RegulonDB` `S` - sigma=sigma32; target=rrfH; function=+
- `activates` --> [[gene.b0209|gene.b0209]] `RegulonDB` `S` - sigma=sigma32; target=yafD; function=+
- `activates` --> [[gene.b0210|gene.b0210]] `RegulonDB` `S` - sigma=sigma32; target=yafE; function=+
- `activates` --> [[gene.b0415|gene.b0415]] `RegulonDB` `S` - sigma=sigma32; target=ribE; function=+
- `activates` --> [[gene.b0416|gene.b0416]] `RegulonDB` `S` - sigma=sigma32; target=nusB; function=+
- `activates` --> [[gene.b0417|gene.b0417]] `RegulonDB` `S` - sigma=sigma32; target=thiL; function=+
- `activates` --> [[gene.b0418|gene.b0418]] `RegulonDB` `S` - sigma=sigma32; target=pgpA; function=+
- `activates` --> [[gene.b0437|gene.b0437]] `RegulonDB` `S` - sigma=sigma32; target=clpP; function=+
- `activates` --> [[gene.b0438|gene.b0438]] `RegulonDB` `S` - sigma=sigma32; target=clpX; function=+
- `activates` --> [[gene.b0441|gene.b0441]] `RegulonDB` `S` - sigma=sigma32; target=ppiD; function=+
- `activates` --> [[gene.b0473|gene.b0473]] `RegulonDB` `S` - sigma=sigma32; target=htpG; function=+
- `activates` --> [[gene.b0657|gene.b0657]] `RegulonDB` `S` - sigma=sigma32; target=lnt; function=+
- `activates` --> [[gene.b0658|gene.b0658]] `RegulonDB` `S` - sigma=sigma32; target=ybeX; function=+
- `activates` --> [[gene.b0659|gene.b0659]] `RegulonDB` `S` - sigma=sigma32; target=ybeY; function=+
- `activates` --> [[gene.b0660|gene.b0660]] `RegulonDB` `S` - sigma=sigma32; target=ybeZ; function=+
- `activates` --> [[gene.b1129|gene.b1129]] `RegulonDB` `S` - sigma=sigma32; target=phoQ; function=+
- `activates` --> [[gene.b1130|gene.b1130]] `RegulonDB` `S` - sigma=sigma32; target=phoP; function=+
- `activates` --> [[gene.b1274|gene.b1274]] `RegulonDB` `S` - sigma=sigma32; target=topA; function=+
- `activates` --> [[gene.b1279|gene.b1279]] `RegulonDB` `S` - sigma=sigma32; target=lapA; function=+
- `activates` --> [[gene.b1280|gene.b1280]] `RegulonDB` `S` - sigma=sigma32; target=lapB; function=+
- `activates` --> [[gene.b1281|gene.b1281]] `RegulonDB` `S` - sigma=sigma32; target=pyrF; function=+
- `activates` --> [[gene.b1282|gene.b1282]] `RegulonDB` `S` - sigma=sigma32; target=yciH; function=+
- `activates` --> [[gene.b1321|gene.b1321]] `RegulonDB` `S` - sigma=sigma32; target=ycjX; function=+
- `activates` --> [[gene.b1322|gene.b1322]] `RegulonDB` `S` - sigma=sigma32; target=ycjF; function=+
- `activates` --> [[gene.b1323|gene.b1323]] `RegulonDB` `S` - sigma=sigma32; target=tyrR; function=+
- `activates` --> [[gene.b1593|gene.b1593]] `RegulonDB` `S` - sigma=sigma32; target=bidA; function=+
- `activates` --> [[gene.b1594|gene.b1594]] `RegulonDB` `S` - sigma=sigma32; target=mlc; function=+
- `activates` --> [[gene.b1664|gene.b1664]] `RegulonDB` `S` - sigma=sigma32; target=ydhQ; function=+
- `activates` --> [[gene.b1779|gene.b1779]] `RegulonDB` `S` - sigma=sigma32; target=gapA; function=+
- `activates` --> [[gene.b1780|gene.b1780]] `RegulonDB` `S` - sigma=sigma32; target=yeaD; function=+
- `activates` --> [[gene.b1814|gene.b1814]] `RegulonDB` `S` - sigma=sigma32; target=sdaA; function=+
- `activates` --> [[gene.b1829|gene.b1829]] `RegulonDB` `S` - sigma=sigma32; target=htpX; function=+
- `activates` --> [[gene.b1838|gene.b1838]] `RegulonDB` `S` - sigma=sigma32; target=pphA; function=+
- `activates` --> [[gene.b2193|gene.b2193]] `RegulonDB` `S` - sigma=sigma32; target=narP; function=+
- `activates` --> [[gene.b2415|gene.b2415]] `RegulonDB` `S` - sigma=sigma32; target=ptsH; function=+
- `activates` --> [[gene.b2416|gene.b2416]] `RegulonDB` `S` - sigma=sigma32; target=ptsI; function=+
- `activates` --> [[gene.b2417|gene.b2417]] `RegulonDB` `S` - sigma=sigma32; target=crr; function=+
- `activates` --> [[gene.b2592|gene.b2592]] `RegulonDB` `S` - sigma=sigma32; target=clpB; function=+
- `activates` --> [[gene.b2700|gene.b2700]] `RegulonDB` `S` - sigma=sigma32; target=pncC; function=+
- `activates` --> [[gene.b2754|gene.b2754]] `RegulonDB` `S` - sigma=sigma32; target=cas2; function=+
- `activates` --> [[gene.b2954|gene.b2954]] `RegulonDB` `S` - sigma=sigma32; target=rdgB; function=+
- `activates` --> [[gene.b2955|gene.b2955]] `RegulonDB` `S` - sigma=sigma32; target=hemW; function=+
- `activates` --> [[gene.b3067|gene.b3067]] `RegulonDB` `S` - sigma=sigma32; target=rpoD; function=+
- `activates` --> [[gene.b3178|gene.b3178]] `RegulonDB` `S` - sigma=sigma32; target=ftsH; function=+
- `activates` --> [[gene.b3179|gene.b3179]] `RegulonDB` `S` - sigma=sigma32; target=rlmE; function=+
- `activates` --> [[gene.b3272|gene.b3272]] `RegulonDB` `S` - sigma=sigma32; target=rrfF; function=+
- `activates` --> [[gene.b3273|gene.b3273]] `RegulonDB` `S` - sigma=sigma32; target=thrV; function=+
- `activates` --> [[gene.b3274|gene.b3274]] `RegulonDB` `S` - sigma=sigma32; target=rrfD; function=+
- `activates` --> [[gene.b3275|gene.b3275]] `RegulonDB` `S` - sigma=sigma32; target=rrlD; function=+
- `activates` --> [[gene.b3276|gene.b3276]] `RegulonDB` `S` - sigma=sigma32; target=alaU; function=+
- `activates` --> [[gene.b3277|gene.b3277]] `RegulonDB` `S` - sigma=sigma32; target=ileU; function=+
- `activates` --> [[gene.b3278|gene.b3278]] `RegulonDB` `S` - sigma=sigma32; target=rrsD; function=+
- `activates` --> [[gene.b3292|gene.b3292]] `RegulonDB` `S` - sigma=sigma32; target=zntR; function=+
- `activates` --> [[gene.b3293|gene.b3293]] `RegulonDB` `S` - sigma=sigma32; target=yhdN; function=+
- `activates` --> [[gene.b3400|gene.b3400]] `RegulonDB` `S` - sigma=sigma32; target=hslR; function=+
- `activates` --> [[gene.b3401|gene.b3401]] `RegulonDB` `S` - sigma=sigma32; target=hslO; function=+
- `activates` --> [[gene.b3414|gene.b3414]] `RegulonDB` `S` - sigma=sigma32; target=nfuA; function=+
- `activates` --> [[gene.b3619|gene.b3619]] `RegulonDB` `S` - sigma=sigma32; target=rfaD; function=+
- `activates` --> [[gene.b3620|gene.b3620]] `RegulonDB` `S` - sigma=sigma32; target=waaF; function=+
- `activates` --> [[gene.b3621|gene.b3621]] `RegulonDB` `S` - sigma=sigma32; target=waaC; function=+
- `activates` --> [[gene.b3622|gene.b3622]] `RegulonDB` `S` - sigma=sigma32; target=waaL; function=+
- `activates` --> [[gene.b3635|gene.b3635]] `RegulonDB` `S` - sigma=sigma32; target=mutM; function=+
- `activates` --> [[gene.b3686|gene.b3686]] `RegulonDB` `S` - sigma=sigma32; target=ibpB; function=+
- `activates` --> [[gene.b3687|gene.b3687]] `RegulonDB` `S` - sigma=sigma32; target=ibpA; function=+
- `activates` --> [[gene.b3931|gene.b3931]] `RegulonDB` `S` - sigma=sigma32; target=hslU; function=+
- `activates` --> [[gene.b3932|gene.b3932]] `RegulonDB` `S` - sigma=sigma32; target=hslV; function=+
- `activates` --> [[gene.b3965|gene.b3965]] `RegulonDB` `S` - sigma=sigma32; target=trmA; function=+
- `activates` --> [[gene.b3968|gene.b3968]] `RegulonDB` `S` - sigma=sigma32; target=rrsB; function=+
- `activates` --> [[gene.b3969|gene.b3969]] `RegulonDB` `S` - sigma=sigma32; target=gltT; function=+
- `activates` --> [[gene.b3970|gene.b3970]] `RegulonDB` `S` - sigma=sigma32; target=rrlB; function=+
- `activates` --> [[gene.b3971|gene.b3971]] `RegulonDB` `S` - sigma=sigma32; target=rrfB; function=+
- `activates` --> [[gene.b3989|gene.b3989]] `RegulonDB` `S` - sigma=sigma32; target=yjaZ; function=+
- `activates` --> [[gene.b4013|gene.b4013]] `RegulonDB` `S` - sigma=sigma32; target=metA; function=+
- `activates` --> [[gene.b4140|gene.b4140]] `RegulonDB` `S` - sigma=sigma32; target=fxsA; function=+
- `activates` --> [[gene.b4170|gene.b4170]] `RegulonDB` `S` - sigma=sigma32; target=mutL; function=+
- `activates` --> [[gene.b4171|gene.b4171]] `RegulonDB` `S` - sigma=sigma32; target=miaA; function=+
- `activates` --> [[gene.b4172|gene.b4172]] `RegulonDB` `S` - sigma=sigma32; target=hfq; function=+
- `activates` --> [[gene.b4173|gene.b4173]] `RegulonDB` `S` - sigma=sigma32; target=hflX; function=+
- `activates` --> [[gene.b4174|gene.b4174]] `RegulonDB` `S` - sigma=sigma32; target=hflK; function=+
- `activates` --> [[gene.b4175|gene.b4175]] `RegulonDB` `S` - sigma=sigma32; target=hflC; function=+
- `activates` --> [[gene.b4258|gene.b4258]] `RegulonDB` `S` - sigma=sigma32; target=valS; function=+
- `activates` --> [[gene.b4259|gene.b4259]] `RegulonDB` `S` - sigma=sigma32; target=holC; function=+
- `activates` --> [[gene.b4397|gene.b4397]] `RegulonDB` `S` - sigma=sigma32; target=creA; function=+
- `activates` --> [[gene.b4398|gene.b4398]] `RegulonDB` `S` - sigma=sigma32; target=creB; function=+
- `activates` --> [[gene.b4399|gene.b4399]] `RegulonDB` `S` - sigma=sigma32; target=creC; function=+
- `activates` --> [[gene.b4433|gene.b4433]] `RegulonDB` `S` - sigma=sigma32; target=sdsR; function=+
- `is_component_of` --> [[complex.ecocyc.RNAP32-CPLX|complex.ecocyc.RNAP32-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3461|gene.b3461]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGB3`
- `KEGG:ecj:JW3426;eco:b3461;ecoc:C3026_18750;`
- `GeneID:89518301;93778530;947970;`
- `GO:GO:0000345; GO:0001000; GO:0001046; GO:0001216; GO:0003677; GO:0005829; GO:0005886; GO:0006310; GO:0006351; GO:0006352; GO:0006355; GO:0009009; GO:0009408; GO:0010468; GO:0016987; GO:0031421; GO:2000142`

## Notes

RNA polymerase sigma factor RpoH (Heat shock regulatory protein F33.4) (RNA polymerase sigma-32 factor)
