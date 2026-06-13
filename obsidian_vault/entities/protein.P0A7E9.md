---
entity_id: "protein.P0A7E9"
entity_type: "protein"
name: "pyrH"
source_database: "UniProt"
source_id: "P0A7E9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:9922246}. Note=Is predominantly localized near the bacterial membranes."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pyrH smbA b0171 JW0166"
---

# pyrH

`protein.P0A7E9`

## Static

- Type: `protein`
- Source: `UniProt:P0A7E9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:9922246}. Note=Is predominantly localized near the bacterial membranes.

## Enriched Summary

FUNCTION: Catalyzes the reversible phosphorylation of UMP to UDP, with ATP as the most efficient phosphate donor. {ECO:0000269|PubMed:7711027}.

## Biological Role

Catalyzes ATP:UMP phosphotransferase (reaction.R00158). Component of UMP kinase (complex.ecocyc.UMPKI-CPLX).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible phosphorylation of UMP to UDP, with ATP as the most efficient phosphate donor. {ECO:0000269|PubMed:7711027}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00158|reaction.R00158]] `KEGG` `database` - via EC:2.7.4.22
- `is_component_of` --> [[complex.ecocyc.UMPKI-CPLX|complex.ecocyc.UMPKI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0171|gene.b0171]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7E9`
- `KEGG:ecj:JW0166;eco:b0171;ecoc:C3026_00780;`
- `GeneID:86862681;93777254;944989;`
- `GO:GO:0005524; GO:0005829; GO:0006221; GO:0006225; GO:0033862; GO:0042802; GO:0044210`
- `EC:2.7.4.22`

## Notes

Uridylate kinase (UK) (EC 2.7.4.22) (Uridine monophosphate kinase) (UMP kinase) (UMPK)
