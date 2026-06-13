---
entity_id: "gene.b3303"
entity_type: "gene"
name: "rpsE"
source_database: "NCBI RefSeq"
source_id: "gene-b3303"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3303"
  - "rpsE"
---

# rpsE

`gene.b3303`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3303`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpsE (gene.b3303) is a gene entity. It encodes rpsE (protein.P0A7W1). Encoded protein function: FUNCTION: With uS4 and uS12 plays an important role in translational accuracy. Many suppressors of streptomycin-dependent mutants of protein uS12 are found in this protein, some but not all of which decrease translational accuracy (ram, ribosomal ambiguity mutations). {ECO:0000269|PubMed:15652481}.; FUNCTION: Located at the back of the 30S subunit body where it stabilizes the conformation of the head with respect to the body. {ECO:0000269|PubMed:15652481}.; FUNCTION: The physical location of this protein suggests it may also play a role in mRNA unwinding by the ribosome, possibly by forming part of a processivity clamp. {ECO:0000269|PubMed:15652481}. EcoCyc product frame: EG10904-MONOMER. EcoCyc synonyms: spc, eps, spcA. Genomic coordinates: 3444726-3445229. EcoCyc protein note: The S5 protein is a component of the 30S subunit of the ribosome. It was suggested that S5 is positioned to have access to the interface between the 30S and 50S subunits of the ribosome . The N-terminal half of S5 contains the sites of mutations that confer resistance to spectinomycin and binds non-specifically to helix 34 of the 16S rRNA . S5 may be involved in modulating the conformation of the 16S rRNA . S5 can be cross-linked to mRNA and tRNA...

## Biological Role

Repressed by rpsH (protein.P0A7W7).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7W1|protein.P0A7W1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A7W7|protein.P0A7W7]] `RegulonDB` `S` - regulator=RpsH; target=rpsE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010823,ECOCYC:EG10904,GeneID:947795`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3444726-3445229:-; feature_type=gene
