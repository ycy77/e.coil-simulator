---
entity_id: "gene.b0436"
entity_type: "gene"
name: "tig"
source_database: "NCBI RefSeq"
source_id: "gene-b0436"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0436"
  - "tig"
---

# tig

`gene.b0436`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0436`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tig (gene.b0436) is a gene entity. It encodes tig (protein.P0A850). Encoded protein function: FUNCTION: Involved in protein export. Acts as a chaperone by maintaining the newly synthesized secretory and non-secretory proteins in an open conformation. Binds to 3 regions of unfolded substrate PhoA, preferring aromatic and hydrophobic residues, keeping it stretched out and unable to form aggregates (PubMed:24812405). Binds to nascent polypeptide chains via ribosomal protein L23 (PubMed:12226666). Functions as a peptidyl-prolyl cis-trans isomerase in vitro, this activity is dispensible in vivo for chaperone activity. {ECO:0000269|PubMed:12226666, ECO:0000269|PubMed:24812405, ECO:0000269|PubMed:8521806, ECO:0000269|PubMed:8633085}. EcoCyc product frame: EG11003-MONOMER. Genomic coordinates: 455133-456431. EcoCyc protein note: Trigger factor (TF) is a ribsome-associated, ATP-independent chaperone that cooperates with downstream proteins such as EG10241-MONOMER DnaK and CPLX0-3934 GroEL-GroES in the folding of newly synthesized cytosolic proteins; TF also interacts with nascent secretory proteins and cooperates with the CPLX0-8046 SecB chaperone to usher a subset of proteins on the post-translational secretory pathway. TF is involved in protection against copper-induced protein aggregation under anaerobic growth conditions...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A850|protein.P0A850]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001511,ECOCYC:EG11003,GeneID:945081`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:455133-456431:+; feature_type=gene
