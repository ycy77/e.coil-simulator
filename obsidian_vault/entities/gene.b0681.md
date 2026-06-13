---
entity_id: "gene.b0681"
entity_type: "gene"
name: "chiP"
source_database: "NCBI RefSeq"
source_id: "gene-b0681"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0681"
  - "chiP"
---

# chiP

`gene.b0681`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0681`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

chiP (gene.b0681) is a gene entity. It encodes chiP (protein.P75733). Encoded protein function: FUNCTION: Involved in the uptake of chitosugars. {ECO:0000305|PubMed:16857666, ECO:0000305|PubMed:19682266}. EcoCyc product frame: G6370-MONOMER. EcoCyc synonyms: ybfM. Genomic coordinates: 708334-709740. EcoCyc protein note: ChiP (formerly YbfM) is an outer membrane porin for chitooligosaccharides . Under standard growth conditions expression of chiP is negatively regulated by the RNA0-123, which acts by an antisense mechanism to silence chiP mRNA in vivo. ChiX RNA binds to a complementary region in the untranslated region of chiP mRNA that includes the Shine-Dalgarno sequence and destabilises the transcript. ChiX mediated regulation of chiP is dependent on the RNA binding protein EG10438-MONOMER Hfq . In the absence of chitosugars chiP expression is repressed by PD00266 NagC. Full induction of ChiP requires removal of both NagC mediated transcriptional repression and ChiX mediated translational repression . In the presence of chitosugars, antisense regulation of ChiX by the chitobiose operon mRNA (chb mRNA, the so-called 'trap mRNA') results in induction of chiP mRNA translation . The intergenic region (IGR) between the first and second gene of the chitobiose operon (chbBCARFG) possesses complementarity to the same region of ChiX that is used for targeting chiP mRNA. Growth of E...

## Biological Role

Repressed by chiX (gene.b4585), nagC (protein.P0AF20).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75733|protein.P75733]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[gene.b4585|gene.b4585]] `RegulonDB` `S` - regulator=ChiX; target=chiP; function=-
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `S` - regulator=NagC; target=chiP; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002323,ECOCYC:G6370,GeneID:945296`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:708334-709740:+; feature_type=gene
