---
entity_id: "protein.P24197"
entity_type: "protein"
name: "ygiD"
source_database: "UniProt"
source_id: "P24197"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:23666480}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ygiD b3039 JW3007"
---

# ygiD

`protein.P24197`

## Static

- Type: `protein`
- Source: `UniProt:P24197`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:23666480}.

## Enriched Summary

FUNCTION: In vitro, opens the cyclic ring of dihydroxy-phenylalanine (DOPA) between carbons 4 and 5, thus producing an unstable seco-DOPA that rearranges nonenzymatically to betalamic acid. The physiological substrate is unknown. {ECO:0000269|PubMed:23666480}. Purified YgiD has 4,5-DOPA dioxygenase activity. The physiological substrate of the enzyme is so far unknown . Expression of ygiD is induced by exposure to hydroquinone; this induction is abolished in a yhaJ mutant . In the E. coli asymptomatic bacteriuria (ABU) strains 83972 and VR50, YgiD is involved in biofilm formation in urine. ygiD expression is upregulated during growth in human urine compared to growth in minimal medium, and a ygiD mutant strains showed reduced biofilm formation in urine .

## Biological Role

Catalyzes RXN-8460 (reaction.ecocyc.RXN-8460).

## Enriched Pathways

- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: In vitro, opens the cyclic ring of dihydroxy-phenylalanine (DOPA) between carbons 4 and 5, thus producing an unstable seco-DOPA that rearranges nonenzymatically to betalamic acid. The physiological substrate is unknown. {ECO:0000269|PubMed:23666480}.

## Pathways

- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-8460|reaction.ecocyc.RXN-8460]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3039|gene.b3039]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24197`
- `KEGG:ecj:JW3007;eco:b3039;`
- `GeneID:946447;`
- `GO:GO:0005737; GO:0008198; GO:0008270; GO:0050297`
- `EC:1.13.11.29`

## Notes

4,5-DOPA dioxygenase extradiol (EC 1.13.11.29)
