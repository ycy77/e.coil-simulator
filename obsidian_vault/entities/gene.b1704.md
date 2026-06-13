---
entity_id: "gene.b1704"
entity_type: "gene"
name: "aroH"
source_database: "NCBI RefSeq"
source_id: "gene-b1704"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1704"
  - "aroH"
---

# aroH

`gene.b1704`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1704`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aroH (gene.b1704) is a gene entity. It encodes aroH (protein.P00887). Encoded protein function: FUNCTION: Stereospecific condensation of phosphoenolpyruvate (PEP) and D-erythrose-4-phosphate (E4P) giving rise to 3-deoxy-D-arabino-heptulosonate-7-phosphate (DAHP). EcoCyc product frame: AROH-MONOMER. Genomic coordinates: 1788435-1789481. EcoCyc protein note: 2-Dehydro-3-deoxyphosphoheptonate aldolase (DAHP synthase) is involved in the first committed step of the chorismate pathway, which leads to the biosynthesis of aromatic amino acids. DAHP synthase catalyzes an aldol reaction between phosphoenolpyruvate and D-erythrose 4-phosphate to generate 3-deoxy-D-arabino-heptulosonate 7-phosphate (DAHP). There are three isozymes of DAHP synthase, each specifically feedback regulated by tyrosine, phenylalanine or tryptophan . DAHP synthase which is sensitive to tryptophan (DAHP synthase (Trp), AroH) is encoded by aroH. All three isozymes are metalloenzymes, and DAHP synthase (Trp) is activated by Fe2+ . There is a high degree of sequence identity (41%) between the three isozymes and the polypeptides are nearly identical in size . In wild-type cells grown in minimal media, DAHP synthase (Phe) makes up about 80% of the total DAHP synthase activity, DAHP synthase (Tyr) makes up about 20%, and DAHP synthase (Trp) makes up about 1%...

## Biological Role

Repressed by trpR (protein.P0A881). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00887|protein.P00887]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=aroH; function=+
- `represses` <-- [[protein.P0A881|protein.P0A881]] `RegulonDB` `S` - regulator=TrpR; target=aroH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005686,ECOCYC:EG10080,GeneID:946229`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1788435-1789481:+; feature_type=gene
