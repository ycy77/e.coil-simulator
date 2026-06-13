---
entity_id: "gene.b4129"
entity_type: "gene"
name: "lysU"
source_database: "NCBI RefSeq"
source_id: "gene-b4129"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4129"
  - "lysU"
---

# lysU

`gene.b4129`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4129`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lysU (gene.b4129) is a gene entity. It encodes lysU (protein.P0A8N5). Encoded protein function: FUNCTION: Can also synthesize a number of adenyl dinucleotides (in particular AppppA). These dinucleotides have been proposed to act as modulators of the heat-shock response and stress response. EcoCyc product frame: LYSU-MONOMER. Genomic coordinates: 4353200-4354717. EcoCyc protein note: The lysine-tRNA ligase LysU is a member of the family of aminoacyl tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. LysU belongs to the subclass IIB of aminoacyl-tRNA synthetases . E. coli contains both a constitutive (LYSS-MONOMER LysS) and an inducible lysyl-tRNA synthetase; lysU encodes the inducible, more thermostable enzyme . LysU may be more error-prone than LysS . LysU catalyzes misacylation of tRNALys with arginine, threonine, methionine, leucine, alanine, serine, and cysteine, although even the most efficient noncognate substrate, arginine, is used with 1600-fold lower catalytic efficiency than the cognate amino acid lysine...

## Biological Role

Repressed by lrp (protein.P0ACJ0), nac (protein.Q47005).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8N5|protein.P0A8N5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=lysU; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=lysU; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013520,ECOCYC:EG10553,GeneID:948645`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4353200-4354717:-; feature_type=gene
