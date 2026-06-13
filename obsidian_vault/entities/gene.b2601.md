---
entity_id: "gene.b2601"
entity_type: "gene"
name: "aroF"
source_database: "NCBI RefSeq"
source_id: "gene-b2601"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2601"
  - "aroF"
---

# aroF

`gene.b2601`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2601`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aroF (gene.b2601) is a gene entity. It encodes aroF (protein.P00888). Encoded protein function: FUNCTION: Stereospecific condensation of phosphoenolpyruvate (PEP) and D-erythrose-4-phosphate (E4P) giving rise to 3-deoxy-D-arabino-heptulosonate-7-phosphate (DAHP). EcoCyc product frame: AROF-MONOMER. Genomic coordinates: 2740080-2741150. EcoCyc protein note: 2-Dehydro-3-deoxyphosphoheptonate aldolase (DAHP synthase) is involved in the first committed step of the chorismate pathway, which leads to the biosynthesis of aromatic amino acids. DAHP synthase catalyzes an aldol reaction between phosphoenolpyruvate and D-erythrose 4-phosphate to generate 3-deoxy-D-arabino-heptulosonate 7-phosphate (DAHP). There are three isozymes of DAHP synthase, each specifically feedback regulated by tyrosine, phenylalanine or tryptophan . DAHP synthase which is sensitive to tyrosine (DAHP synthase (Tyr), AroF) is encoded by aroF. All three isozymes are metalloenzymes and require a divalent metal for catalysis and/or structural integrity. Different metal ions have been found in DAHP synthase (Tyr) in vivo and in pure preparations . There is a high degree of sequence identity (41%) between the three isozymes and the polypeptides are nearly identical in size...

## Biological Role

Repressed by tyrR (protein.P07604), nac (protein.Q47005). Activated by rpoD (protein.P00579), soxR (protein.P0ACS2).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00888|protein.P00888]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=aroF; function=+
- `activates` <-- [[protein.P0ACS2|protein.P0ACS2]] `RegulonDB` `S` - regulator=SoxR; target=aroF; function=+
- `represses` <-- [[protein.P07604|protein.P07604]] `RegulonDB` `S` - regulator=TyrR; target=aroF; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=aroF; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008549,ECOCYC:EG10078,GeneID:947084`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2740080-2741150:-; feature_type=gene
