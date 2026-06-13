---
entity_id: "protein.P0ABR1"
entity_type: "protein"
name: "dinI"
source_database: "UniProt"
source_id: "P0ABR1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dinI b1061 JW1048"
---

# dinI

`protein.P0ABR1`

## Static

- Type: `protein`
- Source: `UniProt:P0ABR1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in SOS regulation. Inhibits RecA by preventing RecA to bind ssDNA. Can displace ssDNA from RecA. The dinI gene was first identified as a chromosomal locus containing a high affinity operator for the LexA repressor . It encodes a small protein with 80 amino acids and a molecular weight of 8.818 KDa . DinI is not detectable during normal growth of the bacteria, but is induced by DNA damage and is dependent on both LexA and RecA . Its function depends on the concentration of the protein. At concentrations that are stoichimetric with those of RecA, DinI protein acts mainly as a positive modulator of RecA function . DinI stabilizes the RecA filament, reducing or preventing disassembly , which does not affect RecA-mediated ATP hydrolysis and LexA co-protease activities. DinI and RecX (a negative modulator of RecA, which blocks RecA filament extension and leads to net filament disassembly) constitute a regulatory network of RecA . When DinI is present at very high concentrations that are superstoichiometric relative to RecA in vivo, it has contradictory effects on RecA. Overexpression of dinI in E. coli mutant leads to increased UV sensitivity . DinI inhibits both the ability of RecA to induce cleavage of UmuD as well as its recombinase activity . DinI binds to active RecA filament and inhibits its coprotease activity, but not its ATPase activity...

## Annotation

FUNCTION: Involved in SOS regulation. Inhibits RecA by preventing RecA to bind ssDNA. Can displace ssDNA from RecA.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1061|gene.b1061]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABR1`
- `KEGG:ecj:JW1048;eco:b1061;ecoc:C3026_06450;`
- `GeneID:93776346;945022;`
- `GO:GO:0006281; GO:0009432; GO:0019899`

## Notes

DNA damage-inducible protein I
