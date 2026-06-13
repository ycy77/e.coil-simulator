---
entity_id: "gene.b3687"
entity_type: "gene"
name: "ibpA"
source_database: "NCBI RefSeq"
source_id: "gene-b3687"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3687"
  - "ibpA"
---

# ibpA

`gene.b3687`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3687`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ibpA (gene.b3687) is a gene entity. It encodes ibpA (protein.P0C054). Encoded protein function: FUNCTION: Associates with aggregated proteins, together with IbpB, to stabilize and protect them from irreversible denaturation and extensive proteolysis during heat shock and oxidative stress. Aggregated proteins bound to the IbpAB complex are more efficiently refolded and reactivated by the ATP-dependent chaperone systems ClpB and DnaK/DnaJ/GrpE. Its activity is ATP-independent. {ECO:0000269|PubMed:12055295, ECO:0000269|PubMed:12071954}. EcoCyc product frame: EG11534-MONOMER. EcoCyc synonyms: hslT, htpN. Genomic coordinates: 3867009-3867422.

## Biological Role

Repressed by ibpA (protein.P0C054). Activated by lrp (protein.P0ACJ0), rpoH (protein.P0AGB3), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C054|protein.P0C054]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=ibpA; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ibpA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0C054|protein.P0C054]] `RegulonDB` `S` - regulator=small heat shock protein IbpA; target=ibpA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012058,ECOCYC:EG11534,GeneID:948200`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3867009-3867422:-; feature_type=gene
