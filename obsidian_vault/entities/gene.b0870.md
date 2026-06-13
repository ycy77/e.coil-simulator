---
entity_id: "gene.b0870"
entity_type: "gene"
name: "ltaE"
source_database: "NCBI RefSeq"
source_id: "gene-b0870"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0870"
  - "ltaE"
---

# ltaE

`gene.b0870`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0870`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ltaE (gene.b0870) is a gene entity. It encodes ltaE (protein.P75823). Encoded protein function: FUNCTION: Catalyzes the cleavage of L-allo-threonine and L-threonine to glycine and acetaldehyde. L-threo-phenylserine and L-erythro-phenylserine are also good substrates. EcoCyc product frame: LTAA-MONOMER. EcoCyc synonyms: ltaA, ybjU. Genomic coordinates: 908293-909294. EcoCyc protein note: The low-specificity L-threonine aldolase (LtaE) can act on both L-threonine and L-allo-threonine as well as L-threo-phenylserine and L-erythro-phenylserine, but does not utilize the D isomers. The enzyme requires pyridoxal phosphate as a cofactor. L-threonine aldolase may serve in an alternative pathway for glycine biosynthesis when the major pathway is disrupted by a mutation in glyA . LtaE was found to be part of a serendipitous metabolic pathway that produces an intermediate of the PYRIDOXSYN-PWY pathway, 4-PHOSPHONOOXY-THREONINE, that lies downstream of PdxB. The pathway diverts 3-phosphohydroxypyruvate from serine biosynthesis. Here, LtaE catalyzes the aldol condensation of glycolaldehyde and glycine to form 4-hydroxy-L-threonine . An ltaE mutant has no growth defect when grown on glucose as the sole source of carbon . LtaE: "low-specificity L-threonine aldolase"

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75823|protein.P75823]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002954,ECOCYC:G6455,GeneID:944955`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:908293-909294:-; feature_type=gene
