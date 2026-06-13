---
entity_id: "protein.P30871"
entity_type: "protein"
name: "ygiF"
source_database: "UniProt"
source_id: "P30871"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ygiF b3054 JW3026"
---

# ygiF

`protein.P30871`

## Static

- Type: `protein`
- Source: `UniProt:P30871`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the hydrolysis of the beta-gamma-phosphoanhydride linkage of triphosphate-containing substrates (inorganic or nucleoside-linked). Catalyzes the hydrolysis of inorganic triphosphate (PPPi), which could be cytotoxic because of its high affinity for calcium ion, thereby interfering with calcium signaling. It also hydrolyzes slowly thiamine triphosphate (ThTP). YgiF is a specific PPPase, but it contributes only marginally to the total PPPase activity in E.coli, where the main enzyme responsible for hydrolysis of PPPi is inorganic pyrophosphatase (PPase). {ECO:0000269|PubMed:22984449}. YgiF belongs to the CYTH (CyaB-Thiamine triphosphatase) family of proteins. The enzyme was shown to be a specific inorganic triphosphatase. However, the majority of inorganic triphosphatase activity in E. coli cells may be due to the activity of CPLX0-243 . The ygiF gene was amplified from E. coli Mach1TM cells (Thermo Fisher Scientific, derived from E. coli W, not K-12; the Mach1TM gene is 98% identical to the K-12 gene), and crystal structures of the protein were solved. The structures show a conserved triphosphate tunnel metalloenzyme (TTM) fold and a second α-helical domain Two metal ion binding sites suggested a two-metal catalytic mechanism, where one metal ion provides substrate coordination and the other enables a nucleophilic attack on the triphosphate substrate...

## Biological Role

Catalyzes triphosphate phosphohydrolase (reaction.R00138), TRIPHOSPHATASE-RXN (reaction.ecocyc.TRIPHOSPHATASE-RXN).

## Annotation

FUNCTION: Involved in the hydrolysis of the beta-gamma-phosphoanhydride linkage of triphosphate-containing substrates (inorganic or nucleoside-linked). Catalyzes the hydrolysis of inorganic triphosphate (PPPi), which could be cytotoxic because of its high affinity for calcium ion, thereby interfering with calcium signaling. It also hydrolyzes slowly thiamine triphosphate (ThTP). YgiF is a specific PPPase, but it contributes only marginally to the total PPPase activity in E.coli, where the main enzyme responsible for hydrolysis of PPPi is inorganic pyrophosphatase (PPase). {ECO:0000269|PubMed:22984449}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00138|reaction.R00138]] `KEGG` `database` - via EC:3.6.1.25
- `catalyzes` --> [[reaction.ecocyc.TRIPHOSPHATASE-RXN|reaction.ecocyc.TRIPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3054|gene.b3054]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30871`
- `KEGG:ecj:JW3026;eco:b3054;ecoc:C3026_16685;`
- `GeneID:947554;`
- `GO:GO:0046872; GO:0050355`
- `EC:3.6.1.25`

## Notes

Inorganic triphosphatase (PPPase) (EC 3.6.1.25) (ORFXE)
