---
entity_id: "protein.P42626"
entity_type: "protein"
name: "yhaM"
source_database: "UniProt"
source_id: "P42626"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yhaM yhaN b4470 JW5518"
---

# yhaM

`protein.P42626`

## Static

- Type: `protein`
- Source: `UniProt:P42626`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Plays a role in L-cysteine detoxification; it has been speculated to be a cysteine desulfhydrase (PubMed:27435271). {ECO:0000303|PubMed:27435271}. CyuA is an EC-4.4.1.28 in E. coli K-12. It is the major anaerobic cysteine-catabolizing enzyme . Contrary to earlier reports, the enzyme does not act in L-cysteine detoxification; rather, together with YHAO-MONOMER the enzyme allows the organism to utilize L-cysteine as the sole nitrogen and carbon/energy source . CyuA shares sequence similarity with dehydratases that have an iron-sulfur (Fe-S) cluster, such as CyuA in TAX-2190, but exhibits higher sensitivity to molecular oxygen exposure. Activity of CyuA purified in an anaerobic chamber was restored when incubated with Fe(II) and dithiothreitol (DTT), a treatment used with dehydratases to reactivate damaged Fe-S clusters . The enzyme is highly specific, and D-cysteine and analogs of L-cysteine are not substrates. In competition studies in vitro, CyuA was found to bind compounds that contained both a thiol and a primary amine group; serine, alanine, leucine, glutathione nor Β-mercaptoethanol are unable to inhibit . The enzyme has a high Km for L-cysteine (200 μM) that ensures that it does not deplete the cysteine pool in the cell (the concentration of L-cysteine in the cytosol is about 55 μM)...

## Biological Role

Catalyzes LCYSDESULF-RXN (reaction.ecocyc.LCYSDESULF-RXN).

## Annotation

FUNCTION: Plays a role in L-cysteine detoxification; it has been speculated to be a cysteine desulfhydrase (PubMed:27435271). {ECO:0000303|PubMed:27435271}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.LCYSDESULF-RXN|reaction.ecocyc.LCYSDESULF-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4470|gene.b4470]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P42626`
- `KEGG:ecj:JW5518;eco:b4470;ecoc:C3026_16965;`
- `GeneID:2847723;`
- `GO:GO:0009093; GO:0019450; GO:0080146; GO:1901367`

## Notes

UPF0597 protein YhaM
