---
entity_id: "protein.P37758"
entity_type: "protein"
name: "narU"
source_database: "UniProt"
source_id: "P37758"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:18691156}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:18691156}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "narU yddF b1469 JW1464"
---

# narU

`protein.P37758`

## Static

- Type: `protein`
- Source: `UniProt:P37758`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:18691156}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:18691156}.

## Enriched Summary

FUNCTION: Catalyzes nitrate uptake, nitrite uptake and nitrite export across the cytoplasmic membrane. May function as a nitrate/H(+) and nitrite/H(+) channel. Could confer a selective advantage during severe nutrient starvation or slow growth. {ECO:0000269|PubMed:11967075, ECO:0000269|PubMed:15667293, ECO:0000269|PubMed:16804183, ECO:0000269|PubMed:18691156}. NarU catalyses nitrate uptake and nitrite export by an unknown mechanism in. NarU is a member of the major facilitator superfamily (MFS) of transporters , and is highly similar to the nitrate:nitrite antiporter NARK-MONOMER "NarK" . narU forms an operon with narZYWV, encoding NITRATREDUCTZ-CPLX . An RPOS-MONOMER "RpoS"-dependent promoter is located upstream of the narU transcription start site . narU expressed from a plasmid restores the ability of a strain lacking narK to export nitrite from the cytoplasm . Δ(narUnarK) strains are defective in nitrate dependent growth; single ΔnarU or ΔnarK strains can import nitrate at rates similar to wild-type. A multicopy plasmid expressing narU complements a narK mutation for nitrite excretion but not uptake . Under anaerobic conditions NarU confers a selective advantage during nitrate starvation or very slow growth...

## Biological Role

Catalyzes nitrate:nitrite antiport (reaction.ecocyc.TRANS-RXN0-239).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes nitrate uptake, nitrite uptake and nitrite export across the cytoplasmic membrane. May function as a nitrate/H(+) and nitrite/H(+) channel. Could confer a selective advantage during severe nutrient starvation or slow growth. {ECO:0000269|PubMed:11967075, ECO:0000269|PubMed:15667293, ECO:0000269|PubMed:16804183, ECO:0000269|PubMed:18691156}.

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-239|reaction.ecocyc.TRANS-RXN0-239]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1469|gene.b1469]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37758`
- `KEGG:ecj:JW1464;eco:b1469;ecoc:C3026_08525;`
- `GeneID:945799;`
- `GO:GO:0005886; GO:0015112; GO:0015514; GO:0015706; GO:0015707; GO:0042128`

## Notes

Nitrate/nitrite transporter NarU (Nitrite extrusion protein 2) (Nitrite facilitator 2)
