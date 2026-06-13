---
entity_id: "gene.b2579"
entity_type: "gene"
name: "grcA"
source_database: "NCBI RefSeq"
source_id: "gene-b2579"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2579"
  - "grcA"
---

# grcA

`gene.b2579`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2579`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

grcA (gene.b2579) is a gene entity. It encodes grcA (protein.P68066). Encoded protein function: FUNCTION: Acts as a radical domain for damaged PFL and possibly other radical proteins. {ECO:0000269|PubMed:11444864}. EcoCyc product frame: EG11784-MONOMER. EcoCyc synonyms: yfiD. Genomic coordinates: 2716066-2716449. EcoCyc protein note: GrcA is a small (14 kDa) glycyl radical enzyme (GRE) that can restore activity of oxygen-damaged PYRUVFORMLY-CPLX pyruvate formate-lyase (PFL). The relatively stable glycyl radical of PFL, which is essential for catalysis, is sensitive to OXYGEN-MOLECULE . Destruction of the glycyl radical by oxygen results in cleavage of the 85 kDa polypeptide to 83 kDa and a 3 kDa fragment and consequent inactivation of the enzyme . A solution structure of GrcA shows a flexible N-terminal domain followed by a C-terminal region with high amino acid sequence similarity to the glycyl radical domain of PFL . GrcA forms a complex with oxygen-damaged PFL enzyme and displaces the damaged C-terminal glycyl radical domain . After activation by PFLACTENZ-MONOMER (PflA), the PFL-GrcA complex has full pyruvate-formate lyase activity both in vitro and in vivo . In an arcA mutant under microaerobic conditions, GrcA contributes 18% of the flux through the pyruvate formate-lyase reaction...

## Biological Role

Repressed by fnr (protein.P0A9E5), pdhR (protein.P0ACL9). Activated by DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), rpoD (protein.P00579), fis (protein.P0A6R3), fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P68066|protein.P68066]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=grcA; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=grcA; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=grcA; function=-+
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=grcA; function=-+
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=grcA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008489,ECOCYC:EG11784,GeneID:947068`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2716066-2716449:-; feature_type=gene
