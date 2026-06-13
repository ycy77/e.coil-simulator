---
entity_id: "protein.P0AE88"
entity_type: "protein"
name: "cpxR"
source_database: "UniProt"
source_id: "P0AE88"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cpxR yiiA b3912 JW3883"
---

# cpxR

`protein.P0AE88`

## Static

- Type: `protein`
- Source: `UniProt:P0AE88`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Response regulator member of the two-component regulatory system CpxA/CpxR which responds to envelope stress response by activating expression of downstream genes including cpxP, degP, dsbA and ppiA (PubMed:7883164, PubMed:9401031). Required for efficient binding of stationary phase cells to hydrophobic surfaces, part of the process of biofilm formation (PubMed:11830644). Induced upon cell surface binding, subsequently induces genes it controls (cpxP, dsbA and spy, degP is only partially induced) (PubMed:11830644). Binds and activates transcription from the degP promoter (PubMed:7883164); binding is enhanced by phosphorylation (PubMed:9401031). This system combats a variety of extracytoplasmic protein-mediated toxicities by increasing the transcription of the periplasmic protease, DegP in concert with sigma factor E (PubMed:7883164), as well as that of CpxP protein. Other downstream effectors may include SrkA (PubMed:23416055). {ECO:0000269|PubMed:11830644, ECO:0000269|PubMed:23416055, ECO:0000269|PubMed:7883164, ECO:0000269|PubMed:9401031}.

## Biological Role

Component of DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Response regulator member of the two-component regulatory system CpxA/CpxR which responds to envelope stress response by activating expression of downstream genes including cpxP, degP, dsbA and ppiA (PubMed:7883164, PubMed:9401031). Required for efficient binding of stationary phase cells to hydrophobic surfaces, part of the process of biofilm formation (PubMed:11830644). Induced upon cell surface binding, subsequently induces genes it controls (cpxP, dsbA and spy, degP is only partially induced) (PubMed:11830644). Binds and activates transcription from the degP promoter (PubMed:7883164); binding is enhanced by phosphorylation (PubMed:9401031). This system combats a variety of extracytoplasmic protein-mediated toxicities by increasing the transcription of the periplasmic protease, DegP in concert with sigma factor E (PubMed:7883164), as well as that of CpxP protein. Other downstream effectors may include SrkA (PubMed:23416055). {ECO:0000269|PubMed:11830644, ECO:0000269|PubMed:23416055, ECO:0000269|PubMed:7883164, ECO:0000269|PubMed:9401031}.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (51)

- `activates` --> [[gene.b0161|gene.b0161]] `RegulonDB` `S` - regulator=CpxR; target=degP; function=+
- `activates` --> [[gene.b0441|gene.b0441]] `RegulonDB` `S` - regulator=CpxR; target=ppiD; function=+
- `activates` --> [[gene.b0460|gene.b0460]] `RegulonDB` `S` - regulator=CpxR; target=hha; function=+
- `activates` --> [[gene.b0461|gene.b0461]] `RegulonDB` `S` - regulator=CpxR; target=tomB; function=+
- `activates` --> [[gene.b0754|gene.b0754]] `RegulonDB` `S` - regulator=CpxR; target=aroG; function=+
- `activates` --> [[gene.b0925|gene.b0925]] `RegulonDB` `S` - regulator=CpxR; target=ldtD; function=+
- `activates` --> [[gene.b0970|gene.b0970]] `RegulonDB` `C` - regulator=CpxR; target=yccA; function=+
- `activates` --> [[gene.b1113|gene.b1113]] `RegulonDB` `S` - regulator=CpxR; target=ldtC; function=+
- `activates` --> [[gene.b1530|gene.b1530]] `RegulonDB` `S` - regulator=CpxR; target=marR; function=+
- `activates` --> [[gene.b1531|gene.b1531]] `RegulonDB` `S` - regulator=CpxR; target=marA; function=+
- `activates` --> [[gene.b1532|gene.b1532]] `RegulonDB` `S` - regulator=CpxR; target=marB; function=+
- `activates` --> [[gene.b1535|gene.b1535]] `RegulonDB` `S` - regulator=CpxR; target=dgcZ; function=+
- `activates` --> [[gene.b1743|gene.b1743]] `RegulonDB` `S` - regulator=CpxR; target=spy; function=+
- `activates` --> [[gene.b1846|gene.b1846]] `RegulonDB` `S` - regulator=CpxR; target=yebE; function=+
- `activates` --> [[gene.b1902|gene.b1902]] `RegulonDB` `S` - regulator=CpxR; target=ftnB; function=+
- `activates` --> [[gene.b2074|gene.b2074]] `RegulonDB` `S` - regulator=CpxR; target=mdtA; function=+
- `activates` --> [[gene.b2075|gene.b2075]] `RegulonDB` `S` - regulator=CpxR; target=mdtB; function=+
- `activates` --> [[gene.b2076|gene.b2076]] `RegulonDB` `S` - regulator=CpxR; target=mdtC; function=+
- `activates` --> [[gene.b2077|gene.b2077]] `RegulonDB` `S` - regulator=CpxR; target=mdtD; function=+
- `activates` --> [[gene.b2078|gene.b2078]] `RegulonDB` `S` - regulator=CpxR; target=baeS; function=+
- `activates` --> [[gene.b2079|gene.b2079]] `RegulonDB` `S` - regulator=CpxR; target=baeR; function=+
- `activates` --> [[gene.b2215|gene.b2215]] `RegulonDB` `S` - regulator=CpxR; target=ompC; function=+
- `activates` --> [[gene.b2470|gene.b2470]] `RegulonDB` `S` - regulator=CpxR; target=acrD; function=+
- `activates` --> [[gene.b2665|gene.b2665]] `RegulonDB` `S` - regulator=CpxR; target=kbp; function=+
- `activates` --> [[gene.b2666|gene.b2666]] `RegulonDB` `S` - regulator=CpxR; target=yqaE; function=+
- `activates` --> [[gene.b3095|gene.b3095]] `RegulonDB` `S` - regulator=CpxR; target=yqjA; function=+
- `activates` --> [[gene.b3096|gene.b3096]] `RegulonDB` `S` - regulator=CpxR; target=mzrA; function=+
- `activates` --> [[gene.b3363|gene.b3363]] `RegulonDB` `C` - regulator=CpxR; target=ppiA; function=+
- `activates` --> [[gene.b3859|gene.b3859]] `RegulonDB` `S` - regulator=CpxR; target=srkA; function=+
- `activates` --> [[gene.b3860|gene.b3860]] `RegulonDB` `S` - regulator=CpxR; target=dsbA; function=+
- `activates` --> [[gene.b3911|gene.b3911]] `RegulonDB` `S` - regulator=CpxR; target=cpxA; function=+
- `activates` --> [[gene.b3912|gene.b3912]] `RegulonDB` `C` - regulator=CpxR; target=cpxR; function=+
- `activates` --> [[gene.b4391|gene.b4391]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4392|gene.b4392]] `RegulonDB` `S` - regulator=CpxR; target=slt; function=+
- `activates` --> [[gene.b4431|gene.b4431]] `RegulonDB` `S` - regulator=CpxR; target=rprA; function=+
- `activates` --> [[gene.b4484|gene.b4484]] `RegulonDB` `S` - regulator=CpxR; target=cpxP; function=+
- `activates` --> [[gene.b4716|gene.b4716]] `RegulonDB` `C` - regulator=CpxR; target=cpxQ; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b0929|gene.b0929]] `RegulonDB` `S` - regulator=CpxR; target=ompF; function=-
- `represses` --> [[gene.b1037|gene.b1037]] `RegulonDB` `S` - regulator=CpxR; target=csgG; function=-
- `represses` --> [[gene.b1038|gene.b1038]] `RegulonDB` `S` - regulator=CpxR; target=csgF; function=-
- `represses` --> [[gene.b1039|gene.b1039]] `RegulonDB` `S` - regulator=CpxR; target=csgE; function=-
- `represses` --> [[gene.b1040|gene.b1040]] `RegulonDB` `S` - regulator=CpxR; target=csgD; function=-
- `represses` --> [[gene.b1887|gene.b1887]] `RegulonDB` `S` - regulator=CpxR; target=cheW; function=-
- `represses` --> [[gene.b1888|gene.b1888]] `RegulonDB` `S` - regulator=CpxR; target=cheA; function=-
- `represses` --> [[gene.b1889|gene.b1889]] `RegulonDB` `S` - regulator=CpxR; target=motB; function=-
- `represses` --> [[gene.b1890|gene.b1890]] `RegulonDB` `S` - regulator=CpxR; target=motA; function=-
- `represses` --> [[gene.b2580|gene.b2580]] `RegulonDB` `S` - regulator=CpxR; target=ung; function=-
- `represses` --> [[gene.b4355|gene.b4355]] `RegulonDB` `S` - regulator=CpxR; target=tsr; function=-
- `represses` --> [[gene.b4438|gene.b4438]] `RegulonDB` `S` - regulator=CpxR; target=cyaR; function=-
- `represses` --> [[gene.b4828|gene.b4828]] `RegulonDB` `S` - regulator=CpxR; target=motR; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3912|gene.b3912]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE88`
- `KEGG:ecj:JW3883;eco:b3912;ecoc:C3026_21155;`
- `GeneID:86861693;93778026;948404;`
- `GO:GO:0000156; GO:0000976; GO:0003700; GO:0005829; GO:0006355; GO:0007155; GO:0010810; GO:0032993; GO:0045892; GO:0045893`

## Notes

Transcriptional regulatory protein CpxR
