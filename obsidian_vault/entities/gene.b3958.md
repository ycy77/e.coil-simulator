---
entity_id: "gene.b3958"
entity_type: "gene"
name: "argC"
source_database: "NCBI RefSeq"
source_id: "gene-b3958"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3958"
  - "argC"
---

# argC

`gene.b3958`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3958`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

argC (gene.b3958) is a gene entity. It encodes argC (protein.P11446). Encoded protein function: FUNCTION: Catalyzes the NADPH-dependent reduction of N-acetyl-5-glutamyl phosphate to yield N-acetyl-L-glutamate 5-semialdehyde. {ECO:0000255|HAMAP-Rule:MF_00150, ECO:0000269|PubMed:13863980}. EcoCyc product frame: N-ACETYLGLUTPREDUCT-MONOMER. EcoCyc synonyms: Arg2. Genomic coordinates: 4155001-4156005. EcoCyc protein note: N-acetylglutamylphosphate reductase (ArgC) carries out the third step in arginine biosynthesis and its subpathway, ornithine biosynthesis. ArgC catalyzes the NADPH-dependent reduction of N-acetylglutamyl-phosphate to yield N-acetyl-L-glutamate 5-semialdehyde . Evolution and recruitment of promiscuous enzymes have been studied using ProA and its ability to replace ArgC .

## Biological Role

Repressed by argR (protein.P0A6D0). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11446|protein.P11446]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=argC; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=argC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012964,ECOCYC:EG10065,GeneID:948455`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4155001-4156005:+; feature_type=gene
