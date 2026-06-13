---
entity_id: "gene.b0640"
entity_type: "gene"
name: "holA"
source_database: "NCBI RefSeq"
source_id: "gene-b0640"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0640"
  - "holA"
---

# holA

`gene.b0640`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0640`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

holA (gene.b0640) is a gene entity. It encodes holA (protein.P28630). Encoded protein function: FUNCTION: Part of the beta sliding clamp loading complex, which hydrolyzes ATP to load the beta clamp onto primed DNA to form the DNA replication pre-initiation complex (PubMed:2040637). DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria. This DNA polymerase also exhibits 3'-5' exonuclease activity. The delta subunit is the wrench that will open the beta subunit dimer, which has been modeled to leave a gap large enough for ssDNA to pass through (PubMed:11525728). The gamma complex (gamma(3),delta,delta') is thought to load beta dimers onto DNA by binding ATP which alters the complex's conformation so it can bind beta sliding clamp dimers and open them at one interface. Primed DNA is recognized, ATP is hydrolyzed releasing the gamma complex and closing the beta sliding clamp ring around the primed DNA (PubMed:9927437). {ECO:0000269|PubMed:2040637, ECO:0000269|PubMed:9927437, ECO:0000305|PubMed:11525728}. EcoCyc product frame: EG11412-MONOMER. Genomic coordinates: 670574-671605. EcoCyc protein note: Some delta subunits exist independent of the CPLX0-3801, possibly playing a role in stripping the CPLX0-3761 from DNA in the absence of the clamp-loader complex...

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28630|protein.P28630]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002192,ECOCYC:EG11412,GeneID:947573`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:670574-671605:-; feature_type=gene
