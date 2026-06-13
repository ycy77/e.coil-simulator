---
entity_id: "gene.b2415"
entity_type: "gene"
name: "ptsH"
source_database: "NCBI RefSeq"
source_id: "gene-b2415"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2415"
  - "ptsH"
---

# ptsH

`gene.b2415`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2415`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ptsH (gene.b2415) is a gene entity. It encodes ptsH (protein.P0AA04). Encoded protein function: FUNCTION: General (non sugar-specific) component of the phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS). This major carbohydrate active-transport system catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The phosphoryl group from phosphoenolpyruvate (PEP) is transferred to the phosphoryl carrier protein HPr by enzyme I. Phospho-HPr then transfers it to the PTS EIIA domain. EcoCyc product frame: PTSH-PHOSPHORYLATED. EcoCyc synonyms: ctr, hpr. Genomic coordinates: 2533764-2534021. EcoCyc protein note: The bacterial phosphoenolpyruvate:sugar phosphotransferase system involves a series of reactions in which phosphorylated protein intermediates are formed. Histidine-containing protein (HPr) is phosphorylated on the Nπ position of the imidazole ring of His15 by CPLX0-7938 "PTS enzyme I" and acts as a phosphoryl donor to the sugar-specific enzymes IIA . EcoCyc protein note: HPr (histidine containing protein ) is one of two sugar-non-specific protein constituents of the phosphoenolpyruvate:sugar phosphotransferase system (PTSsugar)...

## Biological Role

Repressed by crp (protein.P0ACJ8), cra (protein.P0ACP1), mlc (protein.P50456). Activated by FlhDC DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-3930), rpoD (protein.P00579), crp (protein.P0ACJ8), cra (protein.P0ACP1), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA04|protein.P0AA04]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[complex.ecocyc.CPLX0-3930|complex.ecocyc.CPLX0-3930]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ptsH; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ptsH; function=-+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=ptsH; function=-+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=ptsH; function=+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ptsH; function=-+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=ptsH; function=-+
- `represses` <-- [[protein.P50456|protein.P50456]] `RegulonDB` `S` - regulator=Mlc; target=ptsH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007962,ECOCYC:EG10788,GeneID:946886`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2533764-2534021:+; feature_type=gene
