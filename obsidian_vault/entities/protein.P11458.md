---
entity_id: "protein.P11458"
entity_type: "protein"
name: "nadA"
source_database: "UniProt"
source_id: "P11458"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00567, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nadA nicA b0750 JW0733"
---

# nadA

`protein.P11458`

## Static

- Type: `protein`
- Source: `UniProt:P11458`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00567, ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the condensation of iminoaspartate with dihydroxyacetone phosphate to form quinolinate. {ECO:0000255|HAMAP-Rule:MF_00567, ECO:0000269|PubMed:10648170, ECO:0000269|PubMed:15898769, ECO:0000269|PubMed:15967443, ECO:0000269|PubMed:18674537}. Quinolinate synthase catalyzes the second reaction in the de novo biosynthesis of NAD from aspartate, the condensation of IMINOASPARTATE with DIHYDROXY-ACETONE-PHOSPHATE to form QUINOLINATE. NadA was shown to contain an oxygen-sensitive [4Fe-4S] cluster that is required for its activity , explaining the NAD auxotrophy of an G7325 mutant. Reaction mechanisms involving the [4Fe-4S] cluster have been proposed . The conserved C113, C200 and C297 residues are involved in [4Fe-4S] cluster binding . The C291 and C294 residues appear to undergo reversible disulfide bond formation that regulates the activity of the enzyme . The midpoint potential of -264 mV is similar to that of thioredoxin and of the cytosol . Overexpression of NadA of E. coli BL21 (DE3) used in a microbial fuel cell using L-aspartate as the substrate increased production of NAD(H), and resulted in substantially increased voltage (an increase of 360%) . NadA: "NAD biosynthesis" .

## Biological Role

Component of quinolinate synthase (complex.ecocyc.CPLX0-7719).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the condensation of iminoaspartate with dihydroxyacetone phosphate to form quinolinate. {ECO:0000255|HAMAP-Rule:MF_00567, ECO:0000269|PubMed:10648170, ECO:0000269|PubMed:15898769, ECO:0000269|PubMed:15967443, ECO:0000269|PubMed:18674537}.

## Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7719|complex.ecocyc.CPLX0-7719]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0750|gene.b0750]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P11458`
- `KEGG:ecj:JW0733;eco:b0750;ecoc:C3026_03790;`
- `GeneID:945351;`
- `GO:GO:0005829; GO:0008987; GO:0034628; GO:0046872; GO:0051539`
- `EC:2.5.1.72`

## Notes

Quinolinate synthase (EC 2.5.1.72) (Quinolinate synthetase A)
