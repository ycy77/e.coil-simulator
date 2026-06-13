---
entity_id: "gene.b1719"
entity_type: "gene"
name: "thrS"
source_database: "NCBI RefSeq"
source_id: "gene-b1719"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1719"
  - "thrS"
---

# thrS

`gene.b1719`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1719`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thrS (gene.b1719) is a gene entity. It encodes thrS (protein.P0A8M3). Encoded protein function: FUNCTION: Catalyzes the attachment of threonine to tRNA(Thr) in a two-step reaction: L-threonine is first activated by ATP to form Thr-AMP and then transferred to the acceptor end of tRNA(Thr) (PubMed:10881191, PubMed:15079065, PubMed:18997014). The rate-limiting step is amino acid activation in the presence of tRNA (PubMed:18997014). The 2'-OH of the acceptor base (adenine 76, A76) of tRNA(Thr) and His-309 collaborate to transfer L-Thr to the tRNA; substitution of 2'-OH of A76 with hydrogen or fluorine decreases transfer efficiency 760 and 100-fold respectively (PubMed:18997014). The zinc ion in the active site discriminates against charging of the isosteric amino acid valine (PubMed:10881191). Also activates L-serine, but does not detectably transfer it to tRNA(Thr) (PubMed:15079065). Edits incorrectly charged L-seryl-tRNA(Thr) via its editing domain (PubMed:15079065, PubMed:11136973, PubMed:15525511), in a post-transfer reaction probably via water-mediated hydrolysis (PubMed:15525511). {ECO:0000269|PubMed:10319817, ECO:0000269|PubMed:10881191, ECO:0000269|PubMed:11136973, ECO:0000269|PubMed:15079065, ECO:0000269|PubMed:15525511, ECO:0000269|PubMed:18997014}...

## Biological Role

Repressed by threonine—tRNA ligase (complex.ecocyc.THRS-CPLX), thrS (protein.P0A8M3), nac (protein.Q47005).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8M3|protein.P0A8M3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `represses` <-- [[complex.ecocyc.THRS-CPLX|complex.ecocyc.THRS-CPLX]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` <-- [[protein.P0A8M3|protein.P0A8M3]] `RegulonDB` `S` - regulator=threonine&mdash;tRNA ligase; target=thrS; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=thrS; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005736,ECOCYC:EG11001,GeneID:946222`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1800642-1802570:-; feature_type=gene
