---
entity_id: "gene.b1733"
entity_type: "gene"
name: "chbG"
source_database: "NCBI RefSeq"
source_id: "gene-b1733"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1733"
  - "chbG"
---

# chbG

`gene.b1733`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1733`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

chbG (gene.b1733) is a gene entity. It encodes chbG (protein.P37794). Encoded protein function: FUNCTION: ChbG is essential for growth on the acetylated chitooligosaccharides chitobiose and chitotriose but is dispensable for growth on cellobiose and chitosan dimer, the deacetylated form of chitobiose. Deacetylation of chitobiose-6-P and chitotriose-6-P is necessary for both the activation of the chb promoter by the regulatory protein ChbR and the hydrolysis of phosphorylated beta-glucosides by the phospho-beta-glucosidase ChbF. Catalyzes the removal of only one acetyl group from chitobiose-6-P to yield monoacetylchitobiose-6-P, the inducer of ChbR and the substrate of ChbF. It can also use chitobiose and chitotriose as substrates. {ECO:0000269|PubMed:22797760}. EcoCyc product frame: EG12198-MONOMER. EcoCyc synonyms: celG, ydjC. Genomic coordinates: 1816386-1817135. EcoCyc protein note: ChbG is a chitooligosaccharide monodeacetylase encoded as part of the chb operon, which encodes enzymes involved in growth on CHITOBIOSE as the sole source of carbon . A ΔchbG strain is unable to grow on diacetylchitobiose or triacetylchitobiose as the sole source of carbon and energy. A ΔchbF mutant accumulates monoacetylchitobiose-phosphate; recombinant ChbF degrades this accumulated compound to glucosamine-6-phosphate and N-acetylglucosamine...

## Biological Role

Repressed by nagC (protein.P0AF20), chbR (protein.P17410). Activated by lrp (protein.P0ACJ0), crp (protein.P0ACJ8), chbR (protein.P17410).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37794|protein.P37794]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=chbG; function=+
- `activates` <-- [[protein.P17410|protein.P17410]] `RegulonDB` `S` - regulator=ChbR; target=chbG; function=-+
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `C` - regulator=NagC; target=chbG; function=-
- `represses` <-- [[protein.P17410|protein.P17410]] `RegulonDB` `S` - regulator=ChbR; target=chbG; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0005783,ECOCYC:EG12198,GeneID:946231`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1816386-1817135:-; feature_type=gene
