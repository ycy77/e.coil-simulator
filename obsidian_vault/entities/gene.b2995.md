---
entity_id: "gene.b2995"
entity_type: "gene"
name: "hybB"
source_database: "NCBI RefSeq"
source_id: "gene-b2995"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2995"
  - "hybB"
---

# hybB

`gene.b2995`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2995`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hybB (gene.b2995) is a gene entity. It encodes hybB (protein.P37180). Encoded protein function: FUNCTION: Probable b-type cytochrome. EcoCyc product frame: EG11800-MONOMER. Genomic coordinates: 3142986-3144164. EcoCyc protein note: The HybB protein is predicted to be an integral membrane component of hydrogenase 2 . hybB contains a HXXH conserved motif associated with cytochrome b type proteins . HybB contains no conserved histidines that would serve as heme iron ligands . HybB may act as a proton pump during H(2):quinone oxidoreductase activity (and see ). A hybB in-frame deletion mutant cannot grow on glycerol and fumarate as the sole energy sources. However, the HybOHybC complex is correctly targeted to the membrane and active with the artificial electron acceptor benzyl viologen (BV) .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37180|protein.P37180]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=hybB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009830,ECOCYC:EG11800,GeneID:948615`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3142986-3144164:-; feature_type=gene
