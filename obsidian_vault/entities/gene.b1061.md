---
entity_id: "gene.b1061"
entity_type: "gene"
name: "dinI"
source_database: "NCBI RefSeq"
source_id: "gene-b1061"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1061"
  - "dinI"
---

# dinI

`gene.b1061`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1061`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dinI (gene.b1061) is a gene entity. It encodes dinI (protein.P0ABR1). Encoded protein function: FUNCTION: Involved in SOS regulation. Inhibits RecA by preventing RecA to bind ssDNA. Can displace ssDNA from RecA. EcoCyc product frame: G6558-MONOMER. Genomic coordinates: 1121242-1121487. EcoCyc protein note: The dinI gene was first identified as a chromosomal locus containing a high affinity operator for the LexA repressor . It encodes a small protein with 80 amino acids and a molecular weight of 8.818 KDa . DinI is not detectable during normal growth of the bacteria, but is induced by DNA damage and is dependent on both LexA and RecA . Its function depends on the concentration of the protein. At concentrations that are stoichimetric with those of RecA, DinI protein acts mainly as a positive modulator of RecA function . DinI stabilizes the RecA filament, reducing or preventing disassembly , which does not affect RecA-mediated ATP hydrolysis and LexA co-protease activities. DinI and RecX (a negative modulator of RecA, which blocks RecA filament extension and leads to net filament disassembly) constitute a regulatory network of RecA . When DinI is present at very high concentrations that are superstoichiometric relative to RecA in vivo, it has contradictory effects on RecA. Overexpression of dinI in E. coli mutant leads to increased UV sensitivity...

## Biological Role

Repressed by lexA (protein.P0A7C2). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABR1|protein.P0ABR1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dinI; function=+
- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `C` - regulator=LexA; target=dinI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003599,ECOCYC:G6558,GeneID:945022`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1121242-1121487:-; feature_type=gene
