---
entity_id: "gene.b1591"
entity_type: "gene"
name: "dmsD"
source_database: "NCBI RefSeq"
source_id: "gene-b1591"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1591"
  - "dmsD"
---

# dmsD

`gene.b1591`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1591`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dmsD (gene.b1591) is a gene entity. It encodes dmsD (protein.P69853). Encoded protein function: FUNCTION: Required for biogenesis/assembly of DMSO reductase, but not for the interaction of the DmsA signal peptide with the Tat system. May be part of a chaperone cascade complex that facilitates a folding-maturation pathway for the substrate protein. {ECO:0000255|HAMAP-Rule:MF_00940, ECO:0000269|PubMed:11309116, ECO:0000269|PubMed:12527378, ECO:0000269|PubMed:12813051, ECO:0000269|PubMed:20153451}. EcoCyc product frame: G6849-MONOMER. EcoCyc synonyms: ynfI. Genomic coordinates: 1664506-1665120. EcoCyc protein note: DmsD binds to the twin-arginine leaders of certain proteins, including dimethylsulfoxide (DMSO) reductase and trimethylamine N-oxide (TMAO) reductase that are translocated to the cytoplasmic membrane or the periplasm by the Sec-independent system that is termed Mtt (membrane targeting and transport) or more frequently Tat (twin-arginine translocation) . DmsD interacts with the membrane-associated Tat complex under anaerobic but not aerobic growth and is essential for the biogenesis of DMSO reductase . DmsD interacts with the TatB and TatC subunits of the Tat complex . DmsD has been purified, yielding a mixture of at least five different folding forms, three of which bind to the twin-arginine leader sequence of DmsA...

## Biological Role

Repressed by narL (protein.P0AF28). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69853|protein.P69853]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dmsD; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=dmsD; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=dmsD; function=+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=dmsD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005314,ECOCYC:G6849,GeneID:945987`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1664506-1665120:+; feature_type=gene
