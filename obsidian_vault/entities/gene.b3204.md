---
entity_id: "gene.b3204"
entity_type: "gene"
name: "ptsN"
source_database: "NCBI RefSeq"
source_id: "gene-b3204"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3204"
  - "ptsN"
---

# ptsN

`gene.b3204`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3204`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ptsN (gene.b3204) is a gene entity. It encodes ptsN (protein.P69829). Encoded protein function: FUNCTION: Seems to have a role in regulating nitrogen assimilation. {ECO:0000250}. EcoCyc product frame: MONOMER0-4293. EcoCyc synonyms: yhbI, rpoP. Genomic coordinates: 3346578-3347069. EcoCyc protein note: ptsN encodes a protein paralogous to Enzyme IIAfru of the phosphoenolpyruvate (PEP)-dependent carbohydrate phosphotransferase system (PTS) . PtsN regulates the activity or expression of potassium transporters . The PtsN protein, also known as Enzyme IIANtr, is part of a phosphorelay system (PTSNtr) in E. coli K-12 that may have a role in the regulation of nitrogen metabolism although this has been questioned . The PTSNtr has been implicated in the control of a stress-responsive YCGO-MONOMER "CvrA" mediated K+ efflux pathway . PtsN can be phosphorylated in vivo; both the energy coupling phosphotransferases of the Ntr PTS (EG12188-MONOMER PtsP and EG12147-MONOMER Npr) as well as the sugar PTS contribute to the phosphorylation of PtsN . Dephosphorylated PtsN interacts with the potassium transporter TrkA and inhibits its activity . Dephosphorylated PtsN also interacts with the sensor kinase KdpD and stimulates its activity, resulting in increased levels of phosphorylated response regulator KdpE, thereby increasing expression of kdpFABC, a high-affinity potassium transporter...

## Biological Role

Repressed by hfq (protein.P0A6X3), lrp (protein.P0ACJ0). Activated by rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69829|protein.P69829]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=ptsN; function=+
- `represses` <-- [[protein.P0A6X3|protein.P0A6X3]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010520,ECOCYC:EG11682,GeneID:947721`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3346578-3347069:+; feature_type=gene
