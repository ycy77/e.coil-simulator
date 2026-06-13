---
entity_id: "protein.P0ABM5"
entity_type: "protein"
name: "ccmD"
source_database: "UniProt"
source_id: "P0ABM5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ccmD yojM b2198 JW2186"
---

# ccmD

`protein.P0ABM5`

## Static

- Type: `protein`
- Source: `UniProt:P0ABM5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Required for the export of heme to the periplasm for the biogenesis of c-type cytochromes. {ECO:0000305}. CcmD is a small inner membrane protein that is required for the release of holo-CcmE during PWY-8147 "type I cytochrome c biogenesis". ccmD is part of an 8 gene cluster (ccmABCDEFGH) which bears sequence similarity to Bradyrhizobium japonicum genes that are required for the biogenesis of Cytochromes-c "c-type cytochromes"; an E. coli ΔccmA-H mutant strain (EC06) is not able to produce mature c-type cytochromes under anaerobic, nonfermentative growth conditions (see also ). An in-frame ccmD mutant produces very low levels of holo-CCME-MONOMER CcmE (see further ). CcmD is a small membrane protein that contains a single hydrophobic region. The topology of CcmD has been debated; an earlier study proposed that both the N-terminal domain (NTD) and C-terminal domain (CTD) are located in the cytoplasm with the hydrophobic region in the inner leaflet of the inner membrane . However, a later study suggested that the hydrophobic region constitutes a transmembrane domain with the NTD located in the periplasm and the CTD in the cytoplasm . The short N terminus contains a conserved tyrosine (Tyr-17) of unknown function...

## Biological Role

Component of CcmCDE complex (complex.ecocyc.ABC-35-CPLX), CcmABCD release complex (complex.ecocyc.CPLX-9495).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Required for the export of heme to the periplasm for the biogenesis of c-type cytochromes. {ECO:0000305}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ABC-35-CPLX|complex.ecocyc.ABC-35-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX-9495|complex.ecocyc.CPLX-9495]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2198|gene.b2198]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABM5`
- `KEGG:ecj:JW2186;eco:b2198;ecoc:C3026_12285;`
- `GeneID:86947137;93774980;946709;`
- `GO:GO:0005886; GO:0017004; GO:0043190; GO:1903607; GO:1904334`

## Notes

Heme exporter protein D (Cytochrome c-type biogenesis protein CcmD)
