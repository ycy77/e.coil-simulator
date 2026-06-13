---
entity_id: "protein.P0ACB2"
entity_type: "protein"
name: "hemB"
source_database: "UniProt"
source_id: "P0ACB2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hemB ncf b0369 JW0361"
---

# hemB

`protein.P0ACB2`

## Static

- Type: `protein`
- Source: `UniProt:P0ACB2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes an early step in the biosynthesis of tetrapyrroles. Binds two molecules of 5-aminolevulinate per subunit, each at a distinct site, and catalyzes their condensation to form porphobilinogen. Porphobilinogen synthase (HemB) catalyzes the synthesis of porphobilinogen by an asymmetric condensation of two molecules of 5-aminolevulinate (ALA) via a Schiff-base intermediate . suggested that HemB may be feedback-inhibited by protoporphyrinogen IX, an intermediate in the PWY0-1415 heme biosynthesis pathway. HemB is a metalloenzyme that requires Zn2+ for activity . Mg2+ is not required for activity, however, addition results in stimulation of activity . Two distinct metal binding sites have been identified and characterized and correlated with two ALA binding sites . The asymmetry of the condensation reaction is supported by the two unequal ALA binding sites. Binding of ALA to HemB is ordered, binding at the P-site first; structural requirements for substrate binding to the A- and P-sites differ . The Km for each of the two ALA binding sites has been measured . Site-drected mutagenesis of the conserved His residues H126 and H128 resulted in catalytically active enzymes . Mutagenesis of the active site lysine K246, which forms the Schiff base intermediate, results in decreased, but not abolished activity...

## Biological Role

Catalyzes 5-aminolevulinate hydro-lyase (adding 5-aminolevulinate and cyclizing; porphobilinogen-forming) (reaction.R00036). Component of porphobilinogen synthase (complex.ecocyc.PORPHOBILSYNTH-CPLX).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes an early step in the biosynthesis of tetrapyrroles. Binds two molecules of 5-aminolevulinate per subunit, each at a distinct site, and catalyzes their condensation to form porphobilinogen.

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00036|reaction.R00036]] `KEGG` `database` - via EC:4.2.1.24
- `is_component_of` --> [[complex.ecocyc.PORPHOBILSYNTH-CPLX|complex.ecocyc.PORPHOBILSYNTH-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## Incoming Edges (1)

- `encodes` <-- [[gene.b0369|gene.b0369]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACB2`
- `KEGG:ecj:JW0361;eco:b0369;`
- `GeneID:86862920;93777089;945017;`
- `GO:GO:0000287; GO:0004655; GO:0005829; GO:0006782; GO:0006783; GO:0008270`
- `EC:4.2.1.24`

## Notes

Delta-aminolevulinic acid dehydratase (ALAD) (ALADH) (EC 4.2.1.24) (Porphobilinogen synthase)
