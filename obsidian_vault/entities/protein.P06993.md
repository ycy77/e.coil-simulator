---
entity_id: "protein.P06993"
entity_type: "protein"
name: "malT"
source_database: "UniProt"
source_id: "P06993"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "malT malA b3418 JW3381"
---

# malT

`protein.P06993`

## Static

- Type: `protein`
- Source: `UniProt:P06993`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Positively regulates the transcription of the maltose regulon whose gene products are responsible for uptake and catabolism of malto-oligosaccharides (PubMed:2524384, PubMed:2538630, PubMed:3305511, PubMed:7040340). Specifically binds to the promoter region of its target genes, recognizing a short DNA motif called the MalT box (5'-GGA[TG]GA-3') (PubMed:2524384, PubMed:2538630). Displays weak ATPase activity, but this activity is not required for promoter binding (PubMed:2524384). {ECO:0000269|PubMed:2524384, ECO:0000269|PubMed:2538630, ECO:0000269|PubMed:3305511, ECO:0000269|PubMed:7040340}.

## Biological Role

Component of DNA-binding transcriptional activator MalT-maltotriose-ATP (complex.ecocyc.MONOMER0-158).

## Annotation

FUNCTION: Positively regulates the transcription of the maltose regulon whose gene products are responsible for uptake and catabolism of malto-oligosaccharides (PubMed:2524384, PubMed:2538630, PubMed:3305511, PubMed:7040340). Specifically binds to the promoter region of its target genes, recognizing a short DNA motif called the MalT box (5'-GGA[TG]GA-3') (PubMed:2524384, PubMed:2538630). Displays weak ATPase activity, but this activity is not required for promoter binding (PubMed:2524384). {ECO:0000269|PubMed:2524384, ECO:0000269|PubMed:2538630, ECO:0000269|PubMed:3305511, ECO:0000269|PubMed:7040340}.

## Outgoing Edges (10)

- `activates` --> [[gene.b3416|gene.b3416]] `RegulonDB` `C` - regulator=MalT; target=malQ; function=+
- `activates` --> [[gene.b3417|gene.b3417]] `RegulonDB` `C` - regulator=MalT; target=malP; function=+
- `activates` --> [[gene.b4032|gene.b4032]] `RegulonDB` `C` - regulator=MalT; target=malG; function=+
- `activates` --> [[gene.b4033|gene.b4033]] `RegulonDB` `C` - regulator=MalT; target=malF; function=+
- `activates` --> [[gene.b4034|gene.b4034]] `RegulonDB` `C` - regulator=MalT; target=malE; function=+
- `activates` --> [[gene.b4035|gene.b4035]] `RegulonDB` `C` - regulator=MalT; target=malK; function=+
- `activates` --> [[gene.b4036|gene.b4036]] `RegulonDB` `C` - regulator=MalT; target=lamB; function=+
- `activates` --> [[gene.b4037|gene.b4037]] `RegulonDB` `C` - regulator=MalT; target=malM; function=+
- `activates` --> [[gene.b4807|gene.b4807]] `RegulonDB` `C` - regulator=MalT; target=malH; function=+
- `is_component_of` --> [[complex.ecocyc.MONOMER0-158|complex.ecocyc.MONOMER0-158]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b3418|gene.b3418]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06993`
- `KEGG:ecj:JW3381;eco:b3418;ecoc:C3026_18540;`
- `GeneID:947921;`
- `GO:GO:0003677; GO:0003700; GO:0005524; GO:0042802; GO:0045893; GO:0045913; GO:0048031`

## Notes

HTH-type transcriptional regulator MalT (ATP-dependent transcriptional activator MalT)
