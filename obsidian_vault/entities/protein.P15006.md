---
entity_id: "protein.P15006"
entity_type: "protein"
name: "mcrC"
source_database: "UniProt"
source_id: "P15006"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mcrC b4345 JW5789"
---

# mcrC

`protein.P15006`

## Static

- Type: `protein`
- Source: `UniProt:P15006`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Modifies the specificity of McrB restriction by expanding the range of modified sequences restricted. Does not bind to DNA. McrC is the catalytic subunit responsible for DNA cleavage within the McrBC restriction endonuclease complex . McrC was initially proposed to modulate the specificity of McrB . McrC stimulates the GTPase activity of McrB 30-fold . Site-directed mutagenesis of proposed active site residues has shown that the McrC protein harbors the DNA cleavage activity of the McrBC restriction endonuclease . The N-terminal amino acid sequence of purified McrC has been determined . McrC was thought to be required for the restriction of 5-methylcytosine-containing DNA, but not for the restriction of nonglycosylated phage DNA by McrB ; this phenotype was likely due to the fact that the mcrB-1 mutant allele also leads to reduced amounts of McrC . McrC = "modified cytosine restriction C" Reviews:

## Biological Role

Component of McrBC restriction endonuclease (complex.ecocyc.CPLX0-2661).

## Annotation

FUNCTION: Modifies the specificity of McrB restriction by expanding the range of modified sequences restricted. Does not bind to DNA.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2661|complex.ecocyc.CPLX0-2661]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4345|gene.b4345]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15006`
- `KEGG:ecj:JW5789;eco:b4345;`
- `GeneID:948880;`
- `GO:GO:0009307; GO:0032067; GO:1905348`

## Notes

Type IV methyl-directed restriction enzyme EcoKMcrBC (EcoKMcrBC) (Protein McrC)
