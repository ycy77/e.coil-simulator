---
entity_id: "protein.P26616"
entity_type: "protein"
name: "maeA"
source_database: "UniProt"
source_id: "P26616"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "maeA sfcA b1479 JW5238"
---

# maeA

`protein.P26616`

## Static

- Type: `protein`
- Source: `UniProt:P26616`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

NAD-dependent malic enzyme (NAD-ME) (EC 1.1.1.38) E. coli encodes two "malic enzymes" that catalyze the decarboxylation of malate to form pyruvate with concomitant reduction of NAD(P)+. One enzyme, MaeA (described here) requires NAD+, while the other, MALIC-NADP-MONOMER MaeB, requires NADP+ . Metabolic flux through the malic enzymes during aerobic growth on glycerol as the sole source of carbon appears to be essentially zero . In a strain blocked in the fermentative metabolism of pyruvate, overexpressed NAD+-dependent malate dehydrogenase can support growth by catalyzing the normally non-physiological reductive carboxylation of pyruvate to form malate . MaeA is present as a mixture of monomer, homotetramer and homooctamer in solution . Mg2+ and Mn2+ appear to stabilize two different conformational states of the enzyme . MaeA has been engineered to utilize the bioorthogonal co-substrates nicotinamide flucytosine dinucleotide (NFCD) and nicotinamide cytosine dinucleotide (NCD) in place of NAD . A crystal structure of the engineered variant, L310R/Q401C, has been solved . Expression of maeA is induced by growth on acetate . A maeA mutant does not show a defect when grown on acetate; however, a maeB maeA double mutant in a pckA mutant background abolishes growth on acetate...

## Biological Role

Catalyzes (S)-malate:NAD+ oxidoreductase (decarboxylating) (reaction.R00214), oxaloacetate carboxy-lyase (pyruvate-forming) (reaction.R00217). Component of malate dehydrogenase (oxaloacetate-decarboxylating) (complex.ecocyc.MALIC-NAD-CPLX).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NAD-dependent malic enzyme (NAD-ME) (EC 1.1.1.38)

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00214|reaction.R00214]] `KEGG` `database` - via EC:1.1.1.38
- `catalyzes` --> [[reaction.R00217|reaction.R00217]] `KEGG` `database` - via EC:1.1.1.38
- `is_component_of` --> [[complex.ecocyc.MALIC-NAD-CPLX|complex.ecocyc.MALIC-NAD-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1479|gene.b1479]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P26616`
- `KEGG:ecj:JW5238;eco:b1479;ecoc:C3026_08575;`
- `GeneID:946031;`
- `GO:GO:0004470; GO:0004471; GO:0005829; GO:0006094; GO:0006108; GO:0008948; GO:0042802; GO:0046872; GO:0051287`
- `EC:1.1.1.38`

## Notes

NAD-dependent malic enzyme (NAD-ME) (EC 1.1.1.38)
