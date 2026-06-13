---
entity_id: "gene.b3867"
entity_type: "gene"
name: "hemN"
source_database: "NCBI RefSeq"
source_id: "gene-b3867"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3867"
  - "hemN"
---

# hemN

`gene.b3867`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3867`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hemN (gene.b3867) is a gene entity. It encodes hemN (protein.P32131). Encoded protein function: FUNCTION: Involved in the heme biosynthesis. Catalyzes the anaerobic oxidative decarboxylation of propionate groups of rings A and B of coproporphyrinogen III to yield the vinyl groups in protoporphyrinogen IX. It can use NAD or NADP, but NAD is preferred. {ECO:0000269|PubMed:12114526, ECO:0000269|PubMed:7768836}. EcoCyc product frame: HEMN-MONOMER. EcoCyc synonyms: yihJ. Genomic coordinates: 4052045-4053418. EcoCyc protein note: Oxidative decarboxylation of coproporphyrinogen III to protoporphyrinogen IX is catalyzed by two enzymes in E. coli. Under aerobic conditions, the EG12189 hemF gene product is active. Under anaerobic conditions, HemN catalyzes the coproporphyrinogen III dehydrogenase reaction . HemN is monomeric when overproduced and purified under anaerobic conditions and might be membrane-associated in vivo. The enzyme contains an oxygen-sensitive [4Fe-4S] iron-sulfur cluster; mutations in specific residues important for iron-sulfur cluster coordination and catalysis have been analyzed and a catalytic mechanism has been proposed . HemN has been classified as a "Radical SAM" enzyme . S-adenosylmethionine (SAM) is consumed during catalysis; the role of a second SAM binding site in HemN has been investigated by site-directed mutagenesis...

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32131|protein.P32131]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=hemN; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012629,ECOCYC:EG11836,GeneID:948362`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4052045-4053418:+; feature_type=gene
