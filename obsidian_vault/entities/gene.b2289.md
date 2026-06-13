---
entity_id: "gene.b2289"
entity_type: "gene"
name: "lrhA"
source_database: "NCBI RefSeq"
source_id: "gene-b2289"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2289"
  - "lrhA"
---

# lrhA

`gene.b2289`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2289`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lrhA (gene.b2289) is a gene entity. It encodes lrhA (protein.P36771). Encoded protein function: FUNCTION: Not known, does not seem to act on the proton translocating NADH dehydrogenase genes (nuoA-N) which are part of the lrhA operon. EcoCyc product frame: EG12123-MONOMER. EcoCyc synonyms: genR. Genomic coordinates: 2405703-2406641. EcoCyc protein note: LrhA, "LysR homologue A," regulates the transcription of genes involved in the synthesis of type 1 fimbriae . Indirectly, this protein also regulates the transcription of several genes involved in motility, chemotaxis, and flagellum synthesis by directly controlling the expression of the master regulator FlhDC . On the other hand, LrhA also regulates negatively and partially the translation of rpoS through two mechanisms, one of which is RprA dependent and the other one is RprA independent. RprA is a small RNA that regulates positively the translation of rpoS. Both mechanisms of regulation require the presence of the sRNA chaperone Hfq; therefore, it was suggested that another small RNA, in addition to RprA, that regulates rpoS translation is regulated by LrhA . In a gene expression study during the transition from aerobic to anaerobic conditions, part of the regulatory cascade involving the protein LrhA was analyzed...

## Biological Role

Repressed by uhpU (gene.b4829). Activated by lrp (protein.P0ACJ0), lrhA (protein.P36771).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36771|protein.P36771]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=lrhA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P36771|protein.P36771]] `RegulonDB` `S` - regulator=LrhA; target=lrhA; function=+
- `represses` <-- [[gene.b4829|gene.b4829]] `RegulonDB` `S` - regulator=UhpU; target=lrhA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007555,ECOCYC:EG12123,GeneID:946769`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2405703-2406641:-; feature_type=gene
