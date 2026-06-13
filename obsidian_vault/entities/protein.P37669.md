---
entity_id: "protein.P37669"
entity_type: "protein"
name: "wecH"
source_database: "UniProt"
source_id: "P37669"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01949, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01949}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wecH yiaH b3561 JW3533"
---

# wecH

`protein.P37669`

## Static

- Type: `protein`
- Source: `UniProt:P37669`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01949, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01949}.

## Enriched Summary

FUNCTION: Responsible for the incorporation of O-acetyl groups into the enterobacterial common antigen (ECA) trisaccharide repeat units. Catalyzes the acetylation of both cyclic ECA (ECA(CYC)) and phosphoglyceride-linked ECA (ECA(PG)). {ECO:0000269|PubMed:16936038}. Based on its mutant phenotype, WecH is the O-acetyltransferase responsible for the nonstoichiometric addition of O-acetyl groups onto the 6-position of N-acetyl-D-glucosamine residues of the trisaccharide repeat unit of ECACYC and ECAPG. WecH is predicted to be an inner membrane protein with 10 transmembrane segments . Since it is not known at which stage of ECA biosynthesis acetylation occurs, it is not possible at this time to assign a specific reaction to this enzyme. The authors proposed that it is likely that acetylation occurs during the assembly of lipid III on the cytoplasmic face of the inner membrane, prior to the WzxE-mediated translocation of lipid III across the membrane . However, as of 2023 no experimental data exists to support this proposal. wecH is induced when FtsZ ring assembly is inhibited by expression of SulA, though this is not believed to be relevant to cell division .

## Annotation

FUNCTION: Responsible for the incorporation of O-acetyl groups into the enterobacterial common antigen (ECA) trisaccharide repeat units. Catalyzes the acetylation of both cyclic ECA (ECA(CYC)) and phosphoglyceride-linked ECA (ECA(PG)). {ECO:0000269|PubMed:16936038}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b3561|gene.b3561]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37669`
- `KEGG:ecj:JW3533;eco:b3561;ecoc:C3026_19310;`
- `GeneID:93778292;948077;`
- `GO:GO:0005886; GO:0009246; GO:0016413`
- `EC:2.3.1.-`

## Notes

O-acetyltransferase WecH (EC 2.3.1.-)
