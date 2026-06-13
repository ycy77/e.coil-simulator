---
entity_id: "gene.b0754"
entity_type: "gene"
name: "aroG"
source_database: "NCBI RefSeq"
source_id: "gene-b0754"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0754"
  - "aroG"
---

# aroG

`gene.b0754`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0754`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aroG (gene.b0754) is a gene entity. It encodes aroG (protein.P0AB91). Encoded protein function: FUNCTION: Stereospecific condensation of phosphoenolpyruvate (PEP) and D-erythrose-4-phosphate (E4P) giving rise to 3-deoxy-D-arabino-heptulosonate-7-phosphate (DAHP). EcoCyc product frame: AROG-MONOMER. Genomic coordinates: 785633-786685. EcoCyc protein note: 2-Dehydro-3-deoxyphosphoheptonate aldolase (DAHP synthase) is involved in the first committed step of the chorismate pathway, which leads to the biosynthesis of aromatic amino acids. DAHP synthase catalyzes an aldol reaction between phosphoenolpyruvate and D-erythrose 4-phosphate to generate 3-deoxy-D-arabino-heptulosonate 7-phosphate (DAHP). There are three isozymes of DAHP synthase, each specifically feedback regulated by tyrosine, phenylalanine or tryptophan . DAHP synthase which is sensitive to phenylalanine (DAHP synthase (Phe), AroG) is encoded by aroG. All three isozymes are metalloenzymes, and DAHP synthase (Phe) has been shown to contain 1 mol of iron per mol of tetramer . There is a high degree of sequence identity (41%) between the three isozymes and the polypeptides are nearly identical in size . In wild-type cells grown in minimal media, DAHP synthase (Phe) makes up about 80% of the total DAHP synthase activity, DAHP synthase (Tyr) makes up about 20%, and DAHP synthase (Trp) makes up about 1%...

## Biological Role

Repressed by tyrR (protein.P07604), lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0), cpxR (protein.P0AE88).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB91|protein.P0AB91]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=aroG; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=aroG; function=+
- `represses` <-- [[protein.P07604|protein.P07604]] `RegulonDB` `C` - regulator=TyrR; target=aroG; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002560,ECOCYC:EG10079,GeneID:945605`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:785633-786685:+; feature_type=gene
