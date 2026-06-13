---
entity_id: "gene.b2198"
entity_type: "gene"
name: "ccmD"
source_database: "NCBI RefSeq"
source_id: "gene-b2198"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2198"
  - "ccmD"
---

# ccmD

`gene.b2198`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2198`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ccmD (gene.b2198) is a gene entity. It encodes ccmD (protein.P0ABM5). Encoded protein function: FUNCTION: Required for the export of heme to the periplasm for the biogenesis of c-type cytochromes. {ECO:0000305}. EcoCyc product frame: EG12169-MONOMER. EcoCyc synonyms: yojM. Genomic coordinates: 2295377-2295586. EcoCyc protein note: CcmD is a small inner membrane protein that is required for the release of holo-CcmE during PWY-8147 "type I cytochrome c biogenesis". ccmD is part of an 8 gene cluster (ccmABCDEFGH) which bears sequence similarity to Bradyrhizobium japonicum genes that are required for the biogenesis of Cytochromes-c "c-type cytochromes"; an E. coli ΔccmA-H mutant strain (EC06) is not able to produce mature c-type cytochromes under anaerobic, nonfermentative growth conditions (see also ). An in-frame ccmD mutant produces very low levels of holo-CCME-MONOMER CcmE (see further ). CcmD is a small membrane protein that contains a single hydrophobic region. The topology of CcmD has been debated; an earlier study proposed that both the N-terminal domain (NTD) and C-terminal domain (CTD) are located in the cytoplasm with the hydrophobic region in the inner leaflet of the inner membrane . However, a later study suggested that the hydrophobic region constitutes a transmembrane domain with the NTD located in the periplasm and the CTD in the cytoplasm...

## Biological Role

Repressed by narL (protein.P0AF28), narP (protein.P31802). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), modE (protein.P0A9G8), narP (protein.P31802).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABM5|protein.P0ABM5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ccmD; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ccmD; function=+
- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=ccmD; function=+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=ccmD; function=-+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=ccmD; function=-
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=ccmD; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0007273,ECOCYC:EG12169,GeneID:946709`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2295377-2295586:-; feature_type=gene
