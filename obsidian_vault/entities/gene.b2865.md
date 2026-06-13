---
entity_id: "gene.b2865"
entity_type: "gene"
name: "actS"
source_database: "NCBI RefSeq"
source_id: "gene-b2865"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2865"
  - "actS"
---

# actS

`gene.b2865`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2865`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

actS (gene.b2865) is a gene entity. It encodes ygeR (protein.Q46798). Encoded protein function: Uncharacterized lipoprotein YgeR EcoCyc product frame: G7484-MONOMER. EcoCyc synonyms: ygeR. Genomic coordinates: 2999136-2999891. EcoCyc protein note: ActS (formerly YgeR) contains a lipoprotein signal sequence, a LysM (lysin motif) domain (associated with peptidoglycan binding ) and a LytM (lysostaphin/M23 peptidase) domain (also found in EG12297-MONOMER EnvC, EG12111-MONOMER NlpD and EG10013-MONOMER MepM) . ActS is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). ActS has a degenerate LysM domain and does not have peptidoglycan (PG) hydrolase or endopeptidase activity in vitro . Purified ActS activates the amidases NACMURLALAAMI1-MONOMER AmiA, NACMURLALAAMI2-MONOMER AmiB, and G7458-MONOMER AmiC to digest PG in vitro; ActS interacts physically with AmiC and binds peptidoglycan; ActS appears to function under envelope stress conditions and may function to preferentially activate AmiC (see also ). ActS functions as an amidase activator at low pH; ActS promotes AmiB activity at low pH . Deletion of actS exacerbates the division phenotype of an envC nlpD double null mutant . Over-expression of actS restores cell separation in the envC nlpD double null mutant . actS: amidase activator during stress .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46798|protein.Q46798]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009407,ECOCYC:G7484,GeneID:947352`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2999136-2999891:-; feature_type=gene
