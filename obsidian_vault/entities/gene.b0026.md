---
entity_id: "gene.b0026"
entity_type: "gene"
name: "ileS"
source_database: "NCBI RefSeq"
source_id: "gene-b0026"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0026"
  - "ileS"
---

# ileS

`gene.b0026`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0026`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ileS (gene.b0026) is a gene entity. It encodes ileS (protein.P00956). Encoded protein function: FUNCTION: Catalyzes the attachment of isoleucine to tRNA(Ile). As IleRS can inadvertently accommodate and process structurally similar amino acids such as valine, to avoid such errors it has two additional distinct tRNA(Ile)-dependent editing activities. One activity is designated as 'pretransfer' editing and involves the hydrolysis of activated Val-AMP. The other activity is designated 'posttransfer' editing and involves deacylation of mischarged Val-tRNA(Ile). {ECO:0000269|PubMed:10549284, ECO:0000269|PubMed:10889024, ECO:0000269|PubMed:11782529, ECO:0000269|PubMed:11864608, ECO:0000269|PubMed:12515858, ECO:0000269|PubMed:19557155, ECO:0000269|PubMed:3282306, ECO:0000269|PubMed:9554847}. EcoCyc product frame: ILES-MONOMER. EcoCyc synonyms: ilvS. Genomic coordinates: 22391-25207. EcoCyc protein note: Isoleucine-tRNA ligase (IleRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. IleRS belongs to the Class I aminoacyl tRNA synthetases . Specificity determinants within tRNAIle that are important for recognition by IleRS have been identified...

## Biological Role

Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00956|protein.P00956]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ileS; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=ileS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000094,ECOCYC:EG10492,GeneID:944761`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:22391-25207:+; feature_type=gene
