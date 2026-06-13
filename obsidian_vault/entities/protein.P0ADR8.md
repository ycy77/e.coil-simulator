---
entity_id: "protein.P0ADR8"
entity_type: "protein"
name: "ppnN"
source_database: "UniProt"
source_id: "P0ADR8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ppnN ygdH b2795 JW2766"
---

# ppnN

`protein.P0ADR8`

## Static

- Type: `protein`
- Source: `UniProt:P0ADR8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of the N-glycosidic bond of diverse pyrimidine and purine nucleotide 5'-monophosphates, to form ribose 5-phosphate and the corresponding free base. Can use AMP, GMP, IMP, CMP, dTMP and UMP as substrates. Cannot catalyze the reverse reactions. Is required for optimal growth in glucose minimal medium, possibly because it contributes to nucleoside pool homeostasis by degrading excess nucleotides and feeding back the ribose moiety to catabolism. {ECO:0000269|PubMed:27941785}.

## Biological Role

Catalyzes cytidine-5'-monophosphate phosphoribohydrolase (reaction.R00510). Component of nucleotide 5'-monophosphate nucleosidase (complex.ecocyc.CPLX0-8262).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of the N-glycosidic bond of diverse pyrimidine and purine nucleotide 5'-monophosphates, to form ribose 5-phosphate and the corresponding free base. Can use AMP, GMP, IMP, CMP, dTMP and UMP as substrates. Cannot catalyze the reverse reactions. Is required for optimal growth in glucose minimal medium, possibly because it contributes to nucleoside pool homeostasis by degrading excess nucleotides and feeding back the ribose moiety to catabolism. {ECO:0000269|PubMed:27941785}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00510|reaction.R00510]] `KEGG` `database` - via EC:3.2.2.10
- `is_component_of` --> [[complex.ecocyc.CPLX0-8262|complex.ecocyc.CPLX0-8262]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2795|gene.b2795]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADR8`
- `KEGG:ecj:JW2766;eco:b2795;ecoc:C3026_15370;`
- `GeneID:75172879;75203814;947266;`
- `GO:GO:0005829; GO:0008714; GO:0032991; GO:0042802; GO:0047405; GO:0047723; GO:0051289; GO:0097216`
- `EC:3.2.2.-; 3.2.2.10; 3.2.2.4`

## Notes

Pyrimidine/purine nucleotide 5'-monophosphate nucleosidase (EC 3.2.2.-) (EC 3.2.2.10) (AMP nucleosidase) (EC 3.2.2.4) (CMP nucleosidase) (GMP nucleosidase) (IMP nucleosidase) (UMP nucleosidase) (dTMP nucleosidase)
