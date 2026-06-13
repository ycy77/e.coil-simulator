---
entity_id: "gene.b4237"
entity_type: "gene"
name: "nrdG"
source_database: "NCBI RefSeq"
source_id: "gene-b4237"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4237"
  - "nrdG"
---

# nrdG

`gene.b4237`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4237`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nrdG (gene.b4237) is a gene entity. It encodes nrdG (protein.P0A9N8). Encoded protein function: FUNCTION: Activation of anaerobic ribonucleoside-triphosphate reductase under anaerobic conditions by generation of an organic free radical, using S-adenosylmethionine and reduced flavodoxin as cosubstrates to produce 5'-deoxy-adenosine. {ECO:0000269|PubMed:1460049, ECO:0000269|PubMed:7852304, ECO:0000269|PubMed:9305874}. EcoCyc product frame: RNTRACTIV-MONOMER. EcoCyc synonyms: yjgE. Genomic coordinates: 4459900-4460364. EcoCyc protein note: The NrdG activase activates the NrdD anaerobic ribonucleoside-triphosphate reductase under anaerobic conditions . Using site-directed mutagenesis, the participation of three cysteine residues in iron chelation in the (4Fe-4S) cluster of this enzyme was demonstrated, but a fourth ligand remained unidentified . An nrdG null mutant does not grow under entirely anaerobic conditions, but grows under aerobic or microaerophilic conditions due to the activity of NrdA and/or NrdB . The activase forms a multi-enzyme complex with flavodoxin-NADP reductase, S-adenosylmethionine (AdoMet) and the anaerobic ribonucleoside triphosphate reductase itself. The activase contains a 4Fe-4S cluster which is reduced by flavodoxin. AdoMet binds to the activase and is in turn reduced to a radical intermediate...

## Biological Role

Repressed by nrdR (protein.P0A8D0), hns (protein.P0ACF8), nac (protein.Q47005). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9N8|protein.P0A9N8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nrdG; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=nrdG; function=+
- `represses` <-- [[protein.P0A8D0|protein.P0A8D0]] `RegulonDB` `S` - regulator=NrdR; target=nrdG; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=nrdG; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=nrdG; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013860,ECOCYC:G812,GeneID:948757`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4459900-4460364:-; feature_type=gene
