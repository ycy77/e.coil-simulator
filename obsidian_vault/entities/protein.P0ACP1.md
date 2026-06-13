---
entity_id: "protein.P0ACP1"
entity_type: "protein"
name: "cra"
source_database: "UniProt"
source_id: "P0ACP1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cra fruC fruR shl b0080 JW0078"
---

# cra

`protein.P0ACP1`

## Static

- Type: `protein`
- Source: `UniProt:P0ACP1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Global transcriptional regulator, which plays an important role in the regulation of carbon metabolism. Activates transcription of genes encoding biosynthetic and oxidative enzymes (involved in Krebs cycle, glyoxylate shunt and gluconeogenesis, such as ppsA and fbp). Represses genes involved in sugar catabolism, such as fruB, pfkA, pykF and adhE. Binds asymmetrically to the two half-sites of its operator. {ECO:0000269|PubMed:16115199, ECO:0000269|PubMed:8195118, ECO:0000269|PubMed:8230205, ECO:0000269|PubMed:8550429, ECO:0000269|PubMed:8577250, ECO:0000269|PubMed:8858581, ECO:0000269|PubMed:9084760, ECO:0000269|PubMed:9371462}.

## Biological Role

Component of DNA-binding transcriptional dual regulator Cra (complex.ecocyc.PC00061).

## Annotation

FUNCTION: Global transcriptional regulator, which plays an important role in the regulation of carbon metabolism. Activates transcription of genes encoding biosynthetic and oxidative enzymes (involved in Krebs cycle, glyoxylate shunt and gluconeogenesis, such as ppsA and fbp). Represses genes involved in sugar catabolism, such as fruB, pfkA, pykF and adhE. Binds asymmetrically to the two half-sites of its operator. {ECO:0000269|PubMed:16115199, ECO:0000269|PubMed:8195118, ECO:0000269|PubMed:8230205, ECO:0000269|PubMed:8550429, ECO:0000269|PubMed:8577250, ECO:0000269|PubMed:8858581, ECO:0000269|PubMed:9084760, ECO:0000269|PubMed:9371462}.

## Outgoing Edges (79)

- `activates` --> [[gene.b0112|gene.b0112]] `RegulonDB` `S` - regulator=Cra; target=aroP; function=+
- `activates` --> [[gene.b0733|gene.b0733]] `RegulonDB` `S` - regulator=Cra; target=cydA; function=+
- `activates` --> [[gene.b0734|gene.b0734]] `RegulonDB` `S` - regulator=Cra; target=cydB; function=+
- `activates` --> [[gene.b1037|gene.b1037]] `RegulonDB` `C` - regulator=Cra; target=csgG; function=+
- `activates` --> [[gene.b1038|gene.b1038]] `RegulonDB` `S` - regulator=Cra; target=csgF; function=+
- `activates` --> [[gene.b1039|gene.b1039]] `RegulonDB` `S` - regulator=Cra; target=csgE; function=+
- `activates` --> [[gene.b1040|gene.b1040]] `RegulonDB` `S` - regulator=Cra; target=csgD; function=+
- `activates` --> [[gene.b1136|gene.b1136]] `RegulonDB` `S` - regulator=Cra; target=icd; function=+
- `activates` --> [[gene.b1702|gene.b1702]] `RegulonDB` `C` - regulator=Cra; target=ppsA; function=+
- `activates` --> [[gene.b1777|gene.b1777]] `RegulonDB` `C` - regulator=Cra; target=yeaC; function=+
- `activates` --> [[gene.b2007|gene.b2007]] `RegulonDB` `S` - regulator=Cra; target=tmaR; function=+
- `activates` --> [[gene.b2276|gene.b2276]] `RegulonDB` `S` - regulator=Cra; target=nuoN; function=+
- `activates` --> [[gene.b2277|gene.b2277]] `RegulonDB` `S` - regulator=Cra; target=nuoM; function=+
- `activates` --> [[gene.b2278|gene.b2278]] `RegulonDB` `S` - regulator=Cra; target=nuoL; function=+
- `activates` --> [[gene.b2279|gene.b2279]] `RegulonDB` `S` - regulator=Cra; target=nuoK; function=+
- `activates` --> [[gene.b2280|gene.b2280]] `RegulonDB` `S` - regulator=Cra; target=nuoJ; function=+
- `activates` --> [[gene.b2281|gene.b2281]] `RegulonDB` `S` - regulator=Cra; target=nuoI; function=+
- `activates` --> [[gene.b2282|gene.b2282]] `RegulonDB` `S` - regulator=Cra; target=nuoH; function=+
- `activates` --> [[gene.b2283|gene.b2283]] `RegulonDB` `S` - regulator=Cra; target=nuoG; function=+
- `activates` --> [[gene.b2284|gene.b2284]] `RegulonDB` `S` - regulator=Cra; target=nuoF; function=+
- `activates` --> [[gene.b2285|gene.b2285]] `RegulonDB` `S` - regulator=Cra; target=nuoE; function=+
- `activates` --> [[gene.b2286|gene.b2286]] `RegulonDB` `S` - regulator=Cra; target=nuoC; function=+
- `activates` --> [[gene.b2287|gene.b2287]] `RegulonDB` `S` - regulator=Cra; target=nuoB; function=+
- `activates` --> [[gene.b2288|gene.b2288]] `RegulonDB` `S` - regulator=Cra; target=nuoA; function=+
- `activates` --> [[gene.b2388|gene.b2388]] `RegulonDB` `S` - regulator=Cra; target=glk; function=-+
- `activates` --> [[gene.b2415|gene.b2415]] `RegulonDB` `C` - regulator=Cra; target=ptsH; function=-+
- `activates` --> [[gene.b2416|gene.b2416]] `RegulonDB` `C` - regulator=Cra; target=ptsI; function=-+
- `activates` --> [[gene.b2417|gene.b2417]] `RegulonDB` `C` - regulator=Cra; target=crr; function=-+
- `activates` --> [[gene.b3357|gene.b3357]] `RegulonDB` `C` - regulator=Cra; target=crp; function=+
- `activates` --> [[gene.b3403|gene.b3403]] `RegulonDB` `C` - regulator=Cra; target=pck; function=+
- `activates` --> [[gene.b4014|gene.b4014]] `RegulonDB` `C` - regulator=Cra; target=aceB; function=+
- `activates` --> [[gene.b4015|gene.b4015]] `RegulonDB` `C` - regulator=Cra; target=aceA; function=+
- `activates` --> [[gene.b4016|gene.b4016]] `RegulonDB` `C` - regulator=Cra; target=aceK; function=+
- `activates` --> [[gene.b4232|gene.b4232]] `RegulonDB` `S` - regulator=Cra; target=fbp; function=+
- `is_component_of` --> [[complex.ecocyc.PC00061|complex.ecocyc.PC00061]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4
- `represses` --> [[gene.b0070|gene.b0070]] `RegulonDB` `S` - regulator=Cra; target=setA; function=-
- `represses` --> [[gene.b0113|gene.b0113]] `RegulonDB` `S` - regulator=Cra; target=pdhR; function=-
- `represses` --> [[gene.b0114|gene.b0114]] `RegulonDB` `S` - regulator=Cra; target=aceE; function=-
- `represses` --> [[gene.b0115|gene.b0115]] `RegulonDB` `S` - regulator=Cra; target=aceF; function=-
- `represses` --> [[gene.b0116|gene.b0116]] `RegulonDB` `S` - regulator=Cra; target=lpd; function=-
- `represses` --> [[gene.b0315|gene.b0315]] `RegulonDB` `S` - regulator=Cra; target=pdeL; function=-
- `represses` --> [[gene.b0331|gene.b0331]] `RegulonDB` `S` - regulator=Cra; target=prpB; function=-
- `represses` --> [[gene.b0333|gene.b0333]] `RegulonDB` `S` - regulator=Cra; target=prpC; function=-
- `represses` --> [[gene.b0334|gene.b0334]] `RegulonDB` `S` - regulator=Cra; target=prpD; function=-
- `represses` --> [[gene.b0335|gene.b0335]] `RegulonDB` `S` - regulator=Cra; target=prpE; function=-
- `represses` --> [[gene.b1241|gene.b1241]] `RegulonDB` `C` - regulator=Cra; target=adhE; function=-
- `represses` --> [[gene.b1530|gene.b1530]] `RegulonDB` `S` - regulator=Cra; target=marR; function=-
- `represses` --> [[gene.b1531|gene.b1531]] `RegulonDB` `S` - regulator=Cra; target=marA; function=-
- `represses` --> [[gene.b1532|gene.b1532]] `RegulonDB` `S` - regulator=Cra; target=marB; function=-
- `represses` --> [[gene.b1676|gene.b1676]] `RegulonDB` `C` - regulator=Cra; target=pykF; function=-
- `represses` --> [[gene.b1779|gene.b1779]] `RegulonDB` `C` - regulator=Cra; target=gapA; function=-
- `represses` --> [[gene.b1780|gene.b1780]] `RegulonDB` `C` - regulator=Cra; target=yeaD; function=-
- `represses` --> [[gene.b1850|gene.b1850]] `RegulonDB` `C` - regulator=Cra; target=eda; function=-
- `represses` --> [[gene.b1851|gene.b1851]] `RegulonDB` `C` - regulator=Cra; target=edd; function=-
- `represses` --> [[gene.b2097|gene.b2097]] `RegulonDB` `S` - regulator=Cra; target=fbaB; function=-
- `represses` --> [[gene.b2167|gene.b2167]] `RegulonDB` `S` - regulator=Cra; target=fruA; function=-
- `represses` --> [[gene.b2168|gene.b2168]] `RegulonDB` `S` - regulator=Cra; target=fruK; function=-
- `represses` --> [[gene.b2169|gene.b2169]] `RegulonDB` `S` - regulator=Cra; target=fruB; function=-
- `represses` --> [[gene.b2388|gene.b2388]] `RegulonDB` `S` - regulator=Cra; target=glk; function=-+
- `represses` --> [[gene.b2415|gene.b2415]] `RegulonDB` `C` - regulator=Cra; target=ptsH; function=-+
- `represses` --> [[gene.b2416|gene.b2416]] `RegulonDB` `C` - regulator=Cra; target=ptsI; function=-+
- `represses` --> [[gene.b2417|gene.b2417]] `RegulonDB` `C` - regulator=Cra; target=crr; function=-+
- `represses` --> [[gene.b2712|gene.b2712]] `RegulonDB` `C` - regulator=Cra; target=hypF; function=-
- `represses` --> [[gene.b2779|gene.b2779]] `RegulonDB` `S` - regulator=Cra; target=eno; function=-
- `represses` --> [[gene.b2925|gene.b2925]] `RegulonDB` `C` - regulator=Cra; target=fbaA; function=-
- `represses` --> [[gene.b2926|gene.b2926]] `RegulonDB` `C` - regulator=Cra; target=pgk; function=-
- `represses` --> [[gene.b2927|gene.b2927]] `RegulonDB` `C` - regulator=Cra; target=epd; function=-
- `represses` --> [[gene.b3365|gene.b3365]] `RegulonDB` `S` - regulator=Cra; target=nirB; function=-
- `represses` --> [[gene.b3366|gene.b3366]] `RegulonDB` `S` - regulator=Cra; target=nirD; function=-
- `represses` --> [[gene.b3367|gene.b3367]] `RegulonDB` `S` - regulator=Cra; target=nirC; function=-
- `represses` --> [[gene.b3368|gene.b3368]] `RegulonDB` `S` - regulator=Cra; target=cysG; function=-
- `represses` --> [[gene.b3612|gene.b3612]] `RegulonDB` `S` - regulator=Cra; target=gpmM; function=-
- `represses` --> [[gene.b3613|gene.b3613]] `RegulonDB` `S` - regulator=Cra; target=envC; function=-
- `represses` --> [[gene.b3614|gene.b3614]] `RegulonDB` `S` - regulator=Cra; target=yibQ; function=-
- `represses` --> [[gene.b3916|gene.b3916]] `RegulonDB` `C` - regulator=Cra; target=pfkA; function=-
- `represses` --> [[gene.b3919|gene.b3919]] `RegulonDB` `S` - regulator=Cra; target=tpiA; function=-
- `represses` --> [[gene.b4233|gene.b4233]] `RegulonDB` `S` - regulator=Cra; target=mpl; function=-
- `represses` --> [[gene.b4577|gene.b4577]] `RegulonDB` `S` - regulator=Cra; target=sgrS; function=-
- `represses` --> [[gene.b4662|gene.b4662]] `RegulonDB` `S` - regulator=Cra; target=sgrT; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0080|gene.b0080]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACP1`
- `KEGG:ecj:JW0078;eco:b0080;`
- `GeneID:86862590;944804;`
- `GO:GO:0000976; GO:0000987; GO:0003700; GO:0006355; GO:0009750; GO:0042802; GO:2000142`

## Notes

Catabolite repressor/activator (Fructose repressor)
